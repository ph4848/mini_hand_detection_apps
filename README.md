 ## Overview
This project explores hand tracking and gesture recognition using a webcam. It contains three independent applications, each demonstrating a different use of finger detection.

## Applications
main.py — Finger Counter
Detects a hand and counts the number of fingers being held up.

app2.py — Finger Gesture Recognition
Displays a text message when the required number of fingers is raised.

app3.py — Victory Gesture Detection
Recognizes the V-shaped hand gesture and displays the word "Victory".

## Technologies Used
Python — Application development.

MediaPipe — Hand tracking and landmark detection.

OpenCV — Webcam input and visual output.
## Installation
### 1. Clone the repository:    
    git clone "https://github.com/ph4848/mini_hand_detection_apps.git"

    cd mini_hand_detection_apps

### 2. Create a virtual environment:

    python -m venv my_env

    my_env\Scripts\activate

    python -m pip install -r requirements.txt 

## Apps
#### Count fingers:
    python main.py
#### Recognize the required finger count:
    python app2.py
#### Detect the victory gesture:
    python app3.py

#### Make sure your webcam is connected and that the application has permission to access it.

## Requirements
#### Python installed on your computer.
#### A working webcam.
#### The Python packages listed in requirements.txt.
