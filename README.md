# **Indian Sign Language Interpreter**

This project aims to create a **real-time Indian Sign Language (ISL) interpreter** that recognizes both static hand gestures for alphabets (A-Z) and dynamic hand gestures for common phrases like "hello," "goodbye," etc. The interpreter processes live webcam input, identifies hand movements using **MediaPipe**, and outputs the recognized gesture as text via a **Random Forest** machine learning model.

![Sign Language Recognition - Google Chrome 02-10-2024 23_47_08](https://github.com/user-attachments/assets/74db25b2-e568-4610-ad67-48221e1d9116)

This is the frontend screen.

![vlcsnap-2024-10-02-23h42m25s368](https://github.com/user-attachments/assets/cd29828b-7769-43de-a8a3-15c6f5a8f8ef)

Visual preview of the prediction screen (C is being shown in frame).  

Make sure to set `VideoCapture` to **0** for the default laptop webcam, or **1** if using an external webcam.

---

## **Project Overview**

The Indian Sign Language Interpreter is designed to:

- Recognize **static hand gestures** for alphabets (A-Z).
- Identify **dynamic hand gestures** for common phrases such as "hello" and "goodbye."
- **Real-time processing** of webcam input to display the recognized gestures as text.

---

## **Technologies Used**

- **Python 3.8**: For scripting and machine learning.
- **OpenCV**: Captures and preprocesses video input.
- **MediaPipe**: Detects and tracks hand landmarks.
- **Scikit-learn**: Trains the Random Forest classifier.
- **Streamlit**: Builds the interactive web interface.
- **NumPy**: Manages numerical data processing.
- **Pickle**: Saves and loads the trained model.

---

## **Key Features**

1. **Dataset Collection**  
   The dataset is captured via a webcam using `collect_imgs.py`, storing images for both alphabets (A-Z) and dynamic sequences like "hello" and "goodbye." Hand landmarks are extracted from each frame.

2. **Data Preprocessing**  
   The `create_dataset.py` script uses **MediaPipe** to extract hand landmarks (x, y coordinates). The landmarks are converted into features by calculating the distances and angles between various points on the hand.

3. **Model Architecture**  
   A **Random Forest Classifier** is used for gesture recognition, trained on features extracted from the hand landmarks.

4. **Training**  
   Using `train_classifier.py`, the Random Forest model is trained on a dataset of hand landmarks. The features include **distances and angles** between landmarks, yielding **216 features** per hand. 

5. **Prediction and Real-Time Recognition**  
   The trained Random Forest model predicts the recognized sign in real-time from webcam input. Confidence scores are computed, and the gesture with the highest confidence score is shown.

6. **Validation**  
   The model is validated using a **20% test set**, unseen during training. Metrics like accuracy are calculated to ensure the model's performance.

7. **Handling Overfitting**  
   Random Forest naturally prevents overfitting by restricting the depth of trees and training on a diverse dataset. Additional handling can be applied using techniques like data augmentation.

8. **Tools and Libraries**  
   The project uses **MediaPipe** for hand tracking, **Scikit-learn** for Random Forest modeling, **OpenCV** for video capture, and **Streamlit** for frontend display.

9. **Real-Time Application**  
   The project features a **Streamlit-based frontend** for real-time video capture and gesture recognition. It allows users to view their webcam feed while the recognized gesture and its accuracy are displayed on the side.

10. **Deployment Considerations**  
    The model is saved using **Pickle** and can be reloaded for inference during real-time predictions. For real-time usage, the model is optimized for **speed** and can be deployed on various platforms (laptops, edge devices, etc.).

---

## **Model Training**

1. **Data Preprocessing**  
   - Landmarks are extracted from the hand using **MediaPipe**.
   - Features include **216 landmarks** calculated from distances and angles.
  
2. **Training**  
   - The **Random Forest Classifier** is trained with 100 estimators and a maximum depth of 10.
   - Recursive Feature Elimination (**RFE**) is used to optimize the model by selecting the top 20 features.

---

## **How to Run the Project**

1. Clone the repository.
2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ```bash
   streamlit run frontend.py
4. Ensure your webcam is connected. Change cv2.VideoCapture value to 0 for the default laptop webcam or 1 if using an external one.
5. Start the Sign Language Recognition by pressing the Start Video Capture button.

---

## **Project Structure**

- data/                     # Directory to store the image dataset
- theme.streamlit/           # Streamlit theme configuration
- config.toml                # Streamlit UI settings
- collect_imgs.py            # Code for capturing images
- create_dataset.py          # Code for processing images into features
- train_classifier.py        # Code for training the Random Forest model
- prediction.py              # Code for making predictions in real-time
- frontend.py                # Streamlit-based web interface
- model.p                    # Pickle file storing the trained model

---

## **Future Scope**

1. Extend Dataset: Include more dynamic phrases and hand gestures to improve recognition accuracy.
2. Incorporate Dynamic Sign Language: Implement models like LSTM or GRU to handle dynamic gestures over time.
3. Deploy on Edge Devices: Optimize the model for deployment on edge computing devices for faster real-time recognition.
4. Add Speech Recognition: Integrate speech-to-text systems like Whisper API to map spoken words to corresponding signs.
5. Expand to Regional Variants: Adapt the model to recognize regional variants of Indian Sign Language (ISL).

---
