

# Face Detection using OpenCV and Streamlit 
# In this section, we will build a simple face detection app using OpenCV to detect faces from the webcam and Streamlit to create an easy-to-use web interface.

# Step 1: Install and import Libraries

# !pip install opencv-python
import cv2
import streamlit as st

# cv2 (OpenCV): A powerful library for real-time computer vision tasks like face detection.
# streamlit: A framework that turns Python scripts into interactive web apps easily.

    
# Step 2: Load Haar Cascade Classifier

face_cascade = cv2.CascadeClassifier(r"C:\Users\Zione\Documents\haarcascade_frontalface_default.xml")
# This line loads a pre-trained Haar Cascade classifier for detecting faces. The XML file contains data that helps identify facial features.

# Step 3: Detect Faces Function

def detect_faces():
    cap = cv2.VideoCapture(0)  # Open the default webcam
    st.write("Press 'q' to stop face detection.")
    
    while True:
        ret, frame = cap.read()  # Capture frame-by-frame from webcam
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Show the frame with detected faces
        cv2.imshow('Face Detection', frame)
        
        # Break the loop if 'q' key is pressed
        # cv2.waitKey(1) waits for a keypress.
        # & 0xFF ensures compatibility with different platforms.
        # ord('q') checks if the pressed key is 'q'.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close the window
    
# cv2.VideoCapture(0): Opens the webcam (0 means the default webcam).
# cv2.cvtColor(): Converts the captured image to grayscale because the Haar Cascade works better with grayscale images.
# detectMultiScale(): Detects faces in the image. It scales the image and looks for potential matches, returning the coordinates of the faces.
# cv2.rectangle(): Draws rectangles around the detected faces.

    
# Step 4: Streamlit Integration

def app():
    st.title("Face Detection using Viola-Jones Algorithm")
    st.write("Press the button below to start detecting faces from your webcam.")
    
    # Start detecting faces when the button is pressed
    if st.button("Detect Faces"):
        detect_faces()
    
    # Add a button to stop face detection
    if st.button("Stop Detection"):
        st.write("Face detection has been stopped.")  # You can add logic here if needed

        
# st.title() and st.write() are used to create a title and description on the Streamlit app.
# st.button() creates an interactive button that, when clicked, triggers the detect_faces() function.

# Step 5: Run the App

if __name__ == "__main__":
    app()

