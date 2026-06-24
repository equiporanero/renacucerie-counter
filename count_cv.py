#!/usr/bin/env python3
"""
Count tadpoles in tray images using computer vision (contour detection).
Used as fallback when AI vision APIs are rate-limited.
"""
import cv2
import numpy as np
import json
import os
from datetime import datetime, timezone

IMAGE_DIR = "/root/renacuja-counter/public/images"
OUTPUT_FILE = "/root/renacuja-counter/public/data/counts.json"

def count_tadpoles_cv(image_path):
    """Count tadpoles using contour detection and shape analysis."""
    img = cv2.imread(image_path)
    if img is None:
        return 0
    
    # Convert to HSV for better color segmentation
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Tadpoles are typically dark (black/dark gray) against lighter background
    # Try multiple color ranges to capture tadpoles
    # Dark objects
    lower_dark = np.array([0, 0, 0])
    upper_dark = np.array([180, 255, 80])
    mask_dark = cv2.inRange(hsv, lower_dark, upper_dark)
    
    # Also try grayish
    lower_gray = np.array([0, 0, 50])
    upper_gray = np.array([180, 50, 150])
    mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
    
    # Combine masks
    mask = cv2.bitwise_or(mask_dark, mask_gray)
    
    # Clean up with morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter by area - tadpoles should be within a size range
    min_area = 50      # minimum tadpole area in pixels
    max_area = 5000    # maximum tadpole area in pixels
    
    valid_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if min_area < area < max_area:
            # Check aspect ratio (tadpoles are somewhat elongated)
            x, y, w, h = cv2.boundingRect(cnt)
            aspect = max(w, h) / (min(w, h) + 1e-6)
            if aspect < 10:  # not too elongated (could be debris)
                valid_contours.append(cnt)
    
    return len(valid_contours)

def main():
    results = {}
    for i in range(1, 10):
        path = os.path.join(IMAGE_DIR, f"bandeja_{i}.jpg")
        count = count_tadpoles_cv(path)
        results[str(i)] = count
        print(f"bandeja_{i}: {count} tadpoles (CV estimate)")
    
    total = sum(results.values())
    output = {
        "bandejas": results,
        "total": total,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "method": "computer_vision_fallback"
    }
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nTOTAL: {total} tadpoles (CV estimate)")
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
