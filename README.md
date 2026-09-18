# Farm Intruder Detection System

A real-time computer vision system for detecting selected objects using a webcam and YOLOv8. The system is designed as a basic farm monitoring solution that can identify potential intruders or animals through live camera input.

## Overview

The Farm Intruder Detection System uses the YOLOv8 object detection model with OpenCV to process live webcam footage.

The system monitors the camera feed and detects selected objects such as:

- Person
- Dog
- Cow
- Cat
- Buffalo

When a target object is detected, the system keeps track of detections and can trigger an audible alert using the Windows `winsound` module.

## Features

- Real-time webcam-based object detection
- YOLOv8 object detection
- Detection of people and selected animals
- Detection counting
- Configurable detection threshold
- Audible alert mechanism
- Local computer vision processing using OpenCV

## Technologies Used

- Python
- YOLOv8
- Ultralytics
- OpenCV
- Windows `winsound`

## Project Structure

```text
Farm-Intruder-System/
│
├── cam.py
├── yolov8n.pt
├── requirements.txt
├── .gitignore
└── README.md