import cv2
import numpy as np
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import subprocess  # For running the Python script

# Load the face recognizer and face detector
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define colors and font style
color_recognized = (0, 255, 0)  # Green for recognized face
color_unrecognized = (0, 0, 255)  # Red for unrecognized face
font = cv2.FONT_HERSHEY_SIMPLEX
confidence_threshold = 100  # Adjust this threshold as needed

# Tkinter Window Setup
root = tk.Tk()
root.title("Face Recognition System")
root.geometry("800x600")

# Create a label to display the video feed
video_label = Label(root)
video_label.pack()

# Label to display status text
status_label = Label(root, text="Initializing...", font=("Helvetica", 14))
status_label.pack()

# Function to update the Tkinter window with webcam feed
def update_frame():
    ret, frame = cap.read()
    if not ret:
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        color_face = frame[y:y+h, x:x+w]
        
        # Preprocess and recognize the face
        preprocessed_face = preprocess_face(face)
        label, confidence = recognizer.predict(preprocessed_face)

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(face)

        # Define color and text based on confidence
        if confidence < confidence_threshold and len(eyes) >= 2:
            color = color_recognized
            text = 'Welcome Sir'
            run_python_script()  # Run the Python script when the face is recognized
        else:
            color = color_unrecognized
            text = 'Pravesh Nishedh'

        # Draw rectangle around face and eyes, and show text
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, text, (x, y-10), font, 0.9, color, 2, cv2.LINE_AA)

    # Convert the frame to a format Tkinter can use
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_pil = Image.fromarray(frame_rgb)
    frame_tk = ImageTk.PhotoImage(frame_pil)

    # Update the image in the Tkinter label
    video_label.config(image=frame_tk)  # Update image
    video_label.image = frame_tk  # Store reference to image object

    # Call this function again after 10ms to keep the stream running
    video_label.after(10, update_frame)

def preprocess_face(face):
    """Preprocess the face image to improve recognition."""
    face = cv2.equalizeHist(face)  # Histogram equalization
    face = cv2.GaussianBlur(face, (3, 3), 0)  # Blur to reduce noise
    face = cv2.resize(face, (200, 200))  # Resize to standard size
    return face

# Function to run a Python script when recognized
def run_python_script():
    """Runs a Python file when recognized."""
    try:
        # Replace 'your_script.py' with the path to your Python script
        subprocess.run(['python', ''], check=True)
        print("Python script executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")

# Start the video feed
update_frame()

# Start authentication when the button is pressed
def start_auth():
    status_label.config(text="Authentication started...")

def stop_auth():
    status_label.config(text="Authentication stopped")
    cap.release()
    cv2.destroyAllWindows()

# Buttons to control authentication
start_button = tk.Button(root, text="Start Authentication", font=("Helvetica", 12), command=start_auth)
start_button.pack(side=tk.LEFT, padx=10, pady=10)

stop_button = tk.Button(root, text="Stop Authentication", font=("Helvetica", 12), command=stop_auth)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()
