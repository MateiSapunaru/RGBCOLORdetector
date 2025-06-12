import streamlit as st
import cv2
import numpy as np
from PIL import Image


def detect_color(frame: np.ndarray) -> str:
    """Detect the most prominent color in the given BGR frame."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ranges = {
        "Blue": (np.array([100, 150, 50]), np.array([130, 255, 255])),
        "Green": (np.array([40, 70, 70]), np.array([80, 255, 255])),
        "Yellow": (np.array([20, 150, 50]), np.array([30, 255, 255])),
        "Orange": (np.array([10, 150, 50]), np.array([20, 255, 255])),
        "Purple": (np.array([130, 150, 50]), np.array([160, 255, 255])),
        "Cyan": (np.array([80, 150, 50]), np.array([100, 255, 255])),
        "Pink": (np.array([160, 150, 50]), np.array([170, 255, 255])),
    }

    # Red has two ranges in HSV
    red1 = cv2.inRange(hsv, np.array([0, 150, 50]), np.array([10, 255, 255]))
    red2 = cv2.inRange(hsv, np.array([170, 150, 50]), np.array([180, 255, 255]))
    mask_sums = {"Red": int(np.sum(red1) + np.sum(red2))}

    for name, (lower, upper) in ranges.items():
        mask = cv2.inRange(hsv, lower, upper)
        mask_sums[name] = int(np.sum(mask))

    # Return the color with the highest mask sum
    return max(mask_sums, key=mask_sums.get)


st.title("Real-Time Color Detector")

uploaded_image = st.camera_input("Capture an image")

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    color = detect_color(frame)
    st.write(f"Detected color: **{color}**")
    st.image(image, caption="Captured Image")
