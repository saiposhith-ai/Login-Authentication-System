# Face Recognition Authentication System

This project implements a face recognition authentication system using OpenCV's LBPH (Local Binary Patterns Histograms) algorithm. It is divided into two main components:

- **Training Module (`Authentication-F.py`):** Trains the face recognizer using images from a dataset.
- **Authentication Module (`Face-ID.py`):** Uses the trained model to authenticate users via a webcam feed and a Tkinter GUI.

## Features

- **Face Detection:** Uses Haar cascades to detect faces (and eyes in the authentication module).
- **Face Recognition:** Employs the LBPH face recognizer from OpenCV to identify faces.
- **Graphical User Interface:** A Tkinter-based GUI displays the webcam feed and authentication status.
- **Script Execution:** Optionally executes an external Python script upon successful recognition (customize the script path as needed).

## Prerequisites

- Python 3.6 or higher
- A functional webcam

### Required Libraries

Install the following dependencies:

```sh
pip install opencv-contrib-python numpy Pillow
Note: The opencv-contrib-python package is required because the LBPH face recognizer is part of OpenCV's extra modules.

Setup
1. Prepare Your Dataset
Create a folder (e.g., dataset) containing your training images in .jpg format.
Ensure that each image filename includes a label (for example, person1.1.jpg) to denote the identity of the person.
2. Train the Face Recognizer
Run the training script to generate a trained model file (trainer.yml):
sh
Copy
Edit
python Authentication-F.py
The script processes images from your dataset, detects faces, extracts labels from filenames, and trains the recognizer.
3. Run the Authentication System
Once the model is trained, start the authentication module:
sh
Copy
Edit
python Face-ID.py
The GUI window will display the live webcam feed.
When a recognized face is detected (with a confidence below the set threshold and at least two eyes detected), a welcome message is shown and an external Python script can be triggered (update the script path in the code as needed).
How It Works
Training Module (Authentication-F.py):

Scans the dataset directory for .jpg images.
Detects faces using a Haar cascade.
Extracts labels from image filenames.
Trains the LBPH face recognizer and saves the model as trainer.yml.
Authentication Module (Face-ID.py):

Captures video from the webcam.
Detects faces and preprocesses them (histogram equalization, Gaussian blur, and resizing).
Recognizes the face using the trained model.
Displays a green rectangle with a welcome message for recognized faces or a red rectangle with an "Access Denied" message for unrecognized faces.
Provides buttons in the Tkinter GUI to start and stop authentication.
Customization
Adjusting the Confidence Threshold:
Modify the confidence_threshold variable in Face-ID.py to change recognition sensitivity.

Script Execution on Recognition:
Update the subprocess.run call in Face-ID.py with the path to your desired Python script that should run upon successful recognition.

License
This project is licensed under the MIT License.

Acknowledgments
Thanks to the OpenCV community for extensive documentation and support.
Appreciation for the Tkinter and Pillow libraries for simplifying GUI development.
