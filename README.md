![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# Face Detection Camera App

## **Description**
**This Python project utilizes [OpenCV](https://github.com/opencv/opencv-python) to detect faces in real-time through your camera**.
<br>When a face is detected, the app saves a snapshot every 5 seconds and overlays the current date and time, as well as the number of detected faces on the video feed.


## **Features**
- **Real-time Face Detection** : Uses OpenCV to detect faces in the video feed.
- **Snapshot Saving** : Automatically saves a snapshot when a face is detected, at a 5-second interval.
- **Timestamp and Face Count Overlay** : Displays the current date/time and the number of detected faces on the video feed.
- **Configurable Quality** : Allows configuration of the JPEG quality for saved snapshots.

## **Prerequisites**
- **Python 3.x** installed on your machine
- **OpenCv** library
- **os** and **time** libraries (*included with Python*)

## **Installation Instructions**
Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the install command.

1. Clone this repository to your machine.

    ```bash
    git clone https://github.com/0x414854/Face_Detection.git

2. Install the required libraries.

    ```bash
    pip install opencv-python

3. Replace the path in '*initialize_face_cascade*' function with the path to your '***haarcascade_frontalface_default.xml***' file.

    ```python
    face_cascade = initialize_face_cascade("/YOUR/PATH/TO/cv2/data/haarcascade_frontalface_default.xml")

4. Once the installation is complete, you're ready to run the program!

   ```bash
   python3 face_detection.py  

## **Usage Examples**
- Run the Python script.
- The camera will open and start detecting faces in real-time.
- Snapshots will be saved in the "Face_detection" directory every 5 seconds if a face is detected.
- The video feed will display the current date/time and the number of detected faces.
- Press 'q' to quit the application.

## Tree Directory

Face_Detection/
<br>├── face_detection.py
<br>└── README.md

## **License**
This project is licensed under the **MIT License**.

## **Author**
[**0x414854**](https://github.com/0x414854)



