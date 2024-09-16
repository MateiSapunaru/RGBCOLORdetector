import cv2
import numpy as np

# Start video capture
vid = cv2.VideoCapture(0)

while True:
    # Capture current frame
    _, frame = vid.read()

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges in HSV
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([130, 255, 255])

    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80, 255, 255])

    lower_red1 = np.array([0, 150, 50])
    
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 150, 50])
    upper_red2 = np.array([180, 255, 255])

    lower_yellow = np.array([20, 150, 50])
    upper_yellow = np.array([30, 255, 255])

    lower_orange = np.array([10, 150, 50])
    upper_orange = np.array([20, 255, 255])

    lower_purple = np.array([130, 150, 50])
    upper_purple = np.array([160, 255, 255])

    lower_cyan = np.array([80, 150, 50])
    upper_cyan = np.array([100, 255, 255])

    lower_pink = np.array([160, 150, 50])
    upper_pink = np.array([170, 255, 255])

    # Create masks for each color
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
    mask_cyan = cv2.inRange(hsv, lower_cyan, upper_cyan)
    mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)

    # Check which mask has the most pixels (i.e., the most prominent color)
    if np.sum(mask_blue) > max(np.sum(mask_green), np.sum(mask_red), np.sum(mask_yellow),
                               np.sum(mask_orange), np.sum(mask_purple), np.sum(mask_cyan), np.sum(mask_pink)):
        print("Blue")
    elif np.sum(mask_green) > max(np.sum(mask_blue), np.sum(mask_red), np.sum(mask_yellow),
                                  np.sum(mask_orange), np.sum(mask_purple), np.sum(mask_cyan), np.sum(mask_pink)):
        print("Green")
    elif np.sum(mask_red) > max(np.sum(mask_blue), np.sum(mask_green), np.sum(mask_yellow),
                                np.sum(mask_orange), np.sum(mask_purple), np.sum(mask_cyan), np.sum(mask_pink)):
        print("Red")
    elif np.sum(mask_yellow) > max(np.sum(mask_blue), np.sum(mask_green), np.sum(mask_red),
                                   np.sum(mask_orange), np.sum(mask_purple), np.sum(mask_cyan), np.sum(mask_pink)):
        print("Yellow")
    elif np.sum(mask_orange) > max(np.sum(mask_blue), np.sum(mask_green), np.sum(mask_red),
                                   np.sum(mask_yellow), np.sum(mask_purple), np.sum(mask_cyan), np.sum(mask_pink)):
        print("Orange")
    elif np.sum(mask_purple) > max(np.sum(mask_blue), np.sum(mask_green), np.sum(mask_red),
                                   np.sum(mask_yellow), np.sum(mask_orange), np.sum(mask_cyan), np.sum(mask_pink)):
        print("Purple")
    elif np.sum(mask_cyan) > max(np.sum(mask_blue), np.sum(mask_green), np.sum(mask_red),
                                 np.sum(mask_yellow), np.sum(mask_orange), np.sum(mask_purple), np.sum(mask_pink)):
        print("Cyan")
    elif np.sum(mask_pink) > max(np.sum(mask_blue), np.sum(mask_green), np.sum(mask_red),
                                 np.sum(mask_yellow), np.sum(mask_orange), np.sum(mask_purple), np.sum(mask_cyan)):
        print("Pink")

    # Show the video feed
    cv2.imshow("frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close all windows
vid.release()
cv2.destroyAllWindows()
