# Laser Pointer Detection Project

This project implements a Python application using OpenCV to detect a laser pointer through a webcam feed. The application is capable of detecting a laser pointer spot within a range of up to 2 meters, with a tolerance of 10 cm.

## Project Description

This project demonstrates proficiency in computer vision using OpenCV by detecting a laser pointer's light spot in real-time. The detection is achieved by:
- Isolating the laser color (typically red) using HSV color filtering.
- Calculating the distance of the laser spot from the camera using spot size approximation.
- Displaying the distance and indicating if it falls within the specified range of 2 meters ±10 cm.

## Features

- Real-time detection of the laser spot from a webcam feed.
- Calculation of the distance from the camera to the laser spot.
- Visual indication if the laser spot is within the acceptable range.

## How to Run

1. **Requirements**: Install Python and OpenCV.
   ```bash
   pip install opencv-python numpy
