import mediapipe as mp
import numpy as np
import time
import cv2
import pandas as pd
import tensorflow as tf

# Load the pre-trained TensorFlow Lite model
tflite_interpreter = tf.lite.Interpreter(model_path="/home/admin/.local/lib/python3.7/site-packages/KNN-Fall-Detection-main/KNN-Fall-Detection-main/model_quantized.tflite")

# Set the number of threads (e.g., use 4 threads)
tflite_interpreter.set_num_threads(4)

# Initialize the TensorFlow Lite interpreter
tflite_interpreter.allocate_tensors()

# Setup for MediaPipe's Pose module
pose_visualizer = mp.solutions.drawing_utils
landmark_styles = mp.solutions.drawing_styles
pose_tracker = mp.solutions.pose

# Specify the 2D coordinates to be extracted for certain keypoints
selected_keypoints = [
    "nose_x", "nose_y",
    "left_eye_x", "left_eye_y",
    "right_eye_x", "right_eye_y",
    "left_shoulder_x", "left_shoulder_y",
    "right_shoulder_x", "right_shoulder_y",
    "left_hip_x", "left_hip_y",
    "right_hip_x", "right_hip_y"
]

# Initialize video capture from a file
video_input = cv2.VideoCapture("/home/admin/.local/lib/python3.7/site-packages/KNN-Fall-Detection-main/KNN-Fall-Detection-main/Fall_Trim.mp4")

# Begin processing the video using MediaPipe's Pose module
with pose_tracker.Pose(
        static_image_mode=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose_estimator:

    # Set initial time reference for FPS calculation
    previous_frame_time = 0
    keypoint_buffer = []

    while video_input.isOpened():
        # Read frames from the video
        success, frame = video_input.read()
        if not success:
            break

        # Resize and convert the frame for MediaPipe processing
        frame = cv2.resize(frame, (224, 224))
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        pose_results = pose_estimator.process(rgb_frame)

        # Extract keypoints if landmarks are detected
        if pose_results.pose_landmarks:
            for landmark in pose_results.pose_landmarks.landmark:
                keypoint_buffer.extend([landmark.x, landmark.y])

        # Convert the processed frame back for visualization
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
        pose_visualizer.draw_landmarks(frame, pose_results.pose_landmarks, pose_tracker.POSE_CONNECTIONS)

        # Compute FPS and display on the frame
        current_frame_time = time.time()
        frame_rate = 1 / (current_frame_time - previous_frame_time)
        previous_frame_time = current_frame_time
        cv2.putText(frame, f'FPS: {int(frame_rate)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 196, 255), 2)

        cv2.imshow('Pose Detection Viewer', frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
            num_frames = len(keypoint_buffer) // len(selected_keypoints)
            reshaped_keypoints = np.array(keypoint_buffer).reshape(num_frames, len(selected_keypoints))
            keypoint_dataframe = pd.DataFrame(data=reshaped_keypoints, columns=selected_keypoints)
            keypoint_dataframe.to_csv("/home/admin/.local/lib/python3.7/site-packages/KNN-Fall-Detection-main/KNN-Fall-Detection-main/fall_keypoints.csv", encoding='utf-8', index=False)
            break

# Release video resources and close display windows
video_input.release()
cv2.destroyAllWindows()
