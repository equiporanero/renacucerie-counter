#!/usr/bin/env python3.12
"""Count small dark objects in tray images using OpenCV (fixed for cv2 version)."""
import cv2
import numpy as np
import json
import os
from datetime import datetime, timezone

IMAGE_DIR = "/root/renacuja-counter/public/images"
OUTPUT_FILE = "/root/renacuja-counter/public/data/counts.json"

def count_objects(image_path):
    """Count dark objects in bowl using multiple CV techniques."""
    img = cv2.imread(image_path)
    if img is None:
        return 0
    
    h, w = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # --- Find bowl region ---
    # Bowl liquid: moderate saturation, moderate-high value
    lower_bowl = np.array([5, 20, 50], dtype=np.uint8)
    upper_bowl = np.array([50, 180, 255], dtype=np.uint8)
    bowl_mask = cv2.inRange(hsv, lower_bowl, upper_bowl)
    
    # Clean up
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    bowl_mask = cv2.morphologyEx(bowl_mask, cv2.MORPH_CLOSE, kernel, iterations=5)
    bowl_mask = cv2.morphologyEx(bowl_mask, cv2.MORPH_OPEN, kernel, iterations=3)
    
    # Keep largest contour
    contours, _ = cv2.findContours(bowl_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return 0
    
    largest = max(contours, key=cv2.contourArea)
    bowl_mask_clean = np.zeros_like(gray)
    cv2.drawContours(bowl_mask_clean, [largest], -1, 255, -1)
    
    # Erode to avoid edges
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    bowl_mask_clean = cv2.erode(bowl_mask_clean, kernel2, iterations=2)
    
    # --- Find dark objects in bowl ---
    val = hsv[:,:,2]
    
    # Method A: Simple threshold on value within bowl
    bowl_val = cv2.bitwise_and(val, bowl_mask_clean)
    _, dark_a = cv2.threshold(bowl_val, 70, 255, cv2.THRESH_BINARY_INV)
    
    # Method B: Adaptive threshold
    enhanced = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8)).apply(gray)
    enhanced_bowl = cv2.bitwise_and(enhanced, bowl_mask_clean)
    dark_b = cv2.adaptiveThreshold(enhanced_bowl, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 31, 10)
    
    # Method C: K-means darkest cluster
    Z = img.reshape((-1, 3)).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 5
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    segmented = labels.reshape((h, w))
    sorted_idx = np.argsort(centers.sum(axis=1))
    darkest = sorted_idx[0]
    dark_c = ((segmented == darkest) & (bowl_mask_clean > 0)).astype(np.uint8) * 255
    
    # Clean all masks
    kernel3 = np.ones((3, 3), np.uint8)
    
    counts = []
    for dark_mask in [dark_a, dark_b, dark_c]:
        clean = cv2.morphologyEx(dark_mask, cv2.MORPH_OPEN, kernel3, iterations=1)
        clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel3, iterations=1)
        
        cnts, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        valid = 0
        for c in cnts:
            a = cv2.contourArea(c)
            if 15 < a < 400:
                p = cv2.arcLength(c, True)
                if p > 0:
                    circ = 4 * np.pi * a / (p * p)
                    if circ > 0.05:
                        valid += 1
        counts.append(valid)
    
    # Return median
    counts.sort()
    return counts[1]

def main():
    results = {}
    for i in range(1, 10):
        path = os.path.join(IMAGE_DIR, f"bandeja_{i}.jpg")
        count = count_objects(path)
        results[str(i)] = count
        print(f"bandeja_{i}: {count}")
    
    total = sum(results.values())
    output = {
        "bandejas": results,
        "total": total,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "method": "computer_vision_ensemble",
        "note": "OpenRouter free tier exhausted (50/50 requests used). Used local CV as fallback. Counts are estimates."
    }
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nTOTAL: {total} (CV estimate)")
    print(f"Saved to {OUTPUT_FILE}")
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
