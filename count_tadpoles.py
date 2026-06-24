#!/usr/bin/env python3
"""
GRENOUCERIE - Contador de renacuajos con OpenCV
Detecta la bandeja automáticamente y cuenta renacuajos dentro de ella.
Genera imágenes marcadas con círculos verdes y números.
"""

import cv2
import numpy as np
import os
import json
import sys
from datetime import datetime, timezone


def detect_tray(img):
    """
    Detecta la bandeja en la imagen.
    Returns: (tray_mask, success)
    """
    h, w = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)

    # La bandeja es la región más grande y clara
    _, bright = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

    # Morfología agresiva para obtener región sólida
    k_close = np.ones((20, 20), np.uint8)
    bright = cv2.morphologyEx(bright, cv2.MORPH_CLOSE, k_close, iterations=10)
    k_open = np.ones((15, 15), np.uint8)
    bright = cv2.morphologyEx(bright, cv2.MORPH_OPEN, k_open, iterations=5)

    cnts = cv2.findContours(bright, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    tray_mask = np.zeros((h, w), dtype=np.uint8)
    tray_ok = False

    if cnts:
        cnts_sorted = sorted(cnts, key=cv2.contourArea, reverse=True)
        for c in cnts_sorted[:3]:
            area = cv2.contourArea(c)
            if area > (h * w * 0.15):
                eps = 0.02 * cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, eps, True)
                cv2.drawContours(tray_mask, [approx], -1, 255, -1)
                tray_ok = True
                break

    if not tray_ok:
        # Fallback: elipse centrada
        cx, cy = w // 2, h // 2
        axes = (int(w * 0.40), int(h * 0.40))
        cv2.ellipse(tray_mask, (cx, cy), axes, 0, 0, 360, 255, -1)

    return tray_mask, tray_ok


def count_tadpoles(img, tray_mask):
    """
    Cuenta renacuajos dentro de la bandeja.
    Usa múltiples métodos de detección y combina resultados.
    """
    h, w = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    v = hsv[:, :, 2]

    candidates = set()

    # Método 1: Adaptive threshold
    v_masked = cv2.bitwise_and(v, v, mask=tray_mask)
    thresh1 = cv2.adaptiveThreshold(v_masked, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 31, 12)
    thresh1 = cv2.bitwise_and(thresh1, thresh1, mask=tray_mask)
    k = np.ones((2, 2), np.uint8)
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, k, iterations=1)
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, k, iterations=2)

    cnts1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = cnts1[0] if len(cnts1) == 2 else cnts1[1]
    for c in cnts1:
        a = cv2.contourArea(c)
        if 12 < a < 600:
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx, cy = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
                if 0 <= cy < h and 0 <= cx < w and tray_mask[cy, cx] > 0:
                    candidates.add((cx, cy))

    # Método 2: Canny edge detection + contour
    masked_gray = cv2.bitwise_and(v, v, mask=tray_mask)
    edges = cv2.Canny(masked_gray, 30, 100)
    edges = cv2.bitwise_and(edges, edges, mask=tray_mask)
    k2 = np.ones((3, 3), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, k2, iterations=2)

    cnts2 = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = cnts2[0] if len(cnts2) == 2 else cnts2[1]
    for c in cnts2:
        a = cv2.contourArea(c)
        if 10 < a < 500:
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx, cy = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
                if 0 <= cy < h and 0 <= cx < w and tray_mask[cy, cx] > 0:
                    # Solo añadir si está cerca de un candidato existente
                    for (ex, ey) in candidates:
                        if abs(cx - ex) < 15 and abs(cy - ey) < 15:
                            candidates.add((cx, cy))
                            break

    # Filtrar duplicados muy cercanos
    filtered = []
    used = set()
    for (cx, cy) in candidates:
        dup = False
        for (fx, fy) in filtered:
            if abs(cx - fx) < 10 and abs(cy - fy) < 10:
                dup = True
                break
        if not dup:
            filtered.append((cx, cy))

    return filtered


def process_tray(img_path, output_path):
    """
    Procesa una bandeja: detecta, cuenta, marca y guarda.
    """
    img = cv2.imread(img_path)
    if img is None:
        return 0, False

    h, w = img.shape[:2]
    original = img.copy()

    # Detectar bandeja
    tray_mask, tray_ok = detect_tray(img)

    # Dibujar contorno de bandeja
    cnts = cv2.findContours(tray_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    if cnts:
        cv2.drawContours(original, cnts, -1, (255, 0, 0), 3)

    # Contar renacuajos
    tads = count_tadpoles(img, tray_mask)

    # Dibujar marcadores
    result = original.copy()
    for i, (cx, cy) in enumerate(tads):
        cv2.circle(result, (cx, cy), 7, (0, 255, 0), 2)
        cv2.putText(result, str(i + 1), (cx + 10, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)

    # Texto con conteo
    cv2.putText(result, f"RENACUAJOS: {len(tads)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)
    cv2.putText(result, f"Tray: {'OK' if tray_ok else 'FALLBACK'}", (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imwrite(output_path, result)
    return len(tads), tray_ok


def main():
    img_dir = os.path.join(os.path.dirname(__file__), "public", "images")
    out_dir = os.path.join(img_dir, "marked_final")
    os.makedirs(out_dir, exist_ok=True)

    results = {}
    tray_status = {}

    for i in range(1, 10):
        src = os.path.join(img_dir, f"bandeja_{i}.jpg")
        dst = os.path.join(out_dir, f"bandeja_{i}_marked.jpg")

        if not os.path.exists(src):
            print(f"Bandeja {i}: NO ENCONTRADA")
            results[str(i)] = 0
            continue

        count, tray_ok = process_tray(src, dst)
        results[str(i)] = count
        tray_status[str(i)] = tray_ok
        print(f"Bandeja {i}: {count} renacuajos (tray: {'OK' if tray_ok else 'FALLBACK'})")

    total = sum(results.values())
    print(f"\nTotal: {total} renacuajos")

    # Guardar JSON
    output = {
        "bandejas": results,
        "total": total,
        "tray_detection": tray_status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "method": "opencv_multi"
    }

    json_path = os.path.join(os.path.dirname(__file__), "public", "data", "counts.json")
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Resultados guardados en {json_path}")

    return results


if __name__ == "__main__":
    main()
