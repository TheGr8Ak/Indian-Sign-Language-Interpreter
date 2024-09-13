# streamlit_app.py

import streamlit as st
import cv2
import prediction as inf  # Import your prediction logic from inference_classifier.py

st.set_page_config(page_title="Video-Based Sign Language Prediction", page_icon=":video_camera:", layout="wide")

cap = cv2.VideoCapture(1)  # Assuming webcam input

st.title("Video-Based Sign Language Prediction")

run_app = st.button("Run Prediction")

if run_app:
    # Create two columns: one for video and one for text/accuracy, side by side
    col1, col2 = st.columns([2, 1])  # Video on the left (2/3), text on the right (1/3)

    with col1:
        # Create a video frame holder
        frame_holder = st.empty()

    with col2:
        # Create placeholders for predicted text and accuracy
        st.subheader("Predicted Text")
        predicted_text_placeholder = st.empty()  # Placeholder for predicted text

        st.subheader("Accuracy Percentage")
        accuracy_placeholder = st.empty()  # Placeholder for accuracy

    while cap.isOpened():
        ret, frame = cap.read()

        # Use the imported process_frame function for prediction
        predicted_text, accuracy = inf.process_frame(frame)

        # Update placeholders dynamically
        if predicted_text:
            predicted_text_placeholder.text(predicted_text)  # Update predicted text
            accuracy_placeholder.text(f"{accuracy:.2f}%")  # Update accuracy

        # Display video frame in color
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Properly convert BGR to RGB for color display
        frame_holder.image(frame, channels="RGB", width=640)  # Adjust width as needed

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()