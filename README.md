**Real-Time Color Detection**

This project uses a webcam feed to detect and display the most prominent color in real-time. It identifies common colors like blue, green, red, yellow, orange, purple, cyan, and pink by analyzing the HSV (Hue, Saturation, Value) color space.
Requirements

To run this project, you'll need the following libraries:

  opencv-python
  numpy


**How It Works**

   
  The webcam captures frames in real-time.
  Each frame is converted from BGR to HSV color space.
  HSV color ranges are defined for common colors.
  The program creates masks for each color and calculates the pixel sum to determine the most prominent color.
  The detected color is printed to the console.



  The program will open a video feed window. Press 'q' to quit.

**The program detects the following colors:**

  Blue
  
  Green
  
  Red
  
  Yellow
  
  Orange
  
  Purple
  
  Cyan
  
  Pink
