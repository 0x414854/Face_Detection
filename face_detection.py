import cv2
import time
import os

def initialize_face_cascade(cascade_path):
    return cv2.CascadeClassifier(cascade_path)

def initialize_video_capture(device_index=0):
    cap = cv2.VideoCapture(device_index)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        exit()
    return cap

def take_picture_if_face_detected(frame, faces, last_save_time, quality=95, output_dir="Face_detection"):
    current_time = time.time()
    if len(faces) > 0 and current_time - last_save_time >= 5:
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, f"face_detected_{time.strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, quality])
        print(f"Face detected! Photo saved at {time.strftime('%H:%M:%S')}")
        return current_time
    return last_save_time

def detect_faces(gray_frame, face_cascade):
    return face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

def main():
    print(f"Camera opening and face detection on : {time.strftime('%d/%m/%Y')} at {time.strftime('%H:%M:%S')}")

    face_cascade = initialize_face_cascade("/YOUR/PATH/TO/cv2/data/haarcascade_frontalface_default.xml")
    cap = initialize_video_capture()

    last_save_time = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.\nExiting.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(gray, face_cascade)
        num_faces = len(faces)

        cv2.putText(frame, f"Date/Hour : {time.strftime('%d/%m/%Y %H:%M:%S')}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        cv2.putText(frame, f"Detected Faces : {num_faces}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        last_save_time = take_picture_if_face_detected(frame, faces, last_save_time)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("User has quit.")
            break

    print(f"End of camera session on : {time.strftime('%d/%m/%Y')} at {time.strftime('%H:%M:%S')}")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
