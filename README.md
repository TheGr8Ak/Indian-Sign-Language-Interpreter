# ISL-Interpreter
**Indian Sign Language interpreter**

This project aims to develop a real-time Indian Sign Language (ISL) interpreter that recognizes both static alphabets (A-Z) and dynamic hand gestures for common phrases like "hello," "goodbye," etc. 
The project uses MediaPipe for hand landmark extraction and a machine learning model (Random Forest) to classify gestures.

![image](https://github.com/user-attachments/assets/1a05eb3f-fff9-452a-8931-8b2d8e396cd2)

The orange block is where the webcam video is displayed. 

Change the value of videocapture to 0 for default laptop webcam.

Otherwise 1 if using an external webcam.



**Project Overview**

The Indian Sign Language Interpreter is designed to recognize:

Static hand gestures for the alphabet (A-Z).

Dynamic hand gestures for common phrases such as "hello" and "goodbye."

It processes live webcam input to identify hand movements and outputs the recognized gesture as text.



**Technologies Used**

Python 3.8

OpenCV: For capturing video input from the webcam.

MediaPipe: For detecting and tracking hand landmarks.

Scikit-learn: For training the Random Forest classifier.

Streamlit: For building the interactive web interface.

NumPy: For handling numerical data processing.

Pickle: For saving and loading the trained model.



**Model Architecture**

The model used for gesture recognition is a Random Forest Classifier trained on hand landmark data. 

The steps include:

Data Preprocessing: Extract distances and angles between hand landmarks for each frame.

Training: A Random Forest model is trained using the extracted features.

Prediction: The model predicts the gesture (alphabet or dynamic sequence) in real-time.
