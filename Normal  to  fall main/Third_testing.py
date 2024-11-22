import cv2
import mediapipe as mp
import numpy as np
import time
import joblib

# Load the trained KNN model for classification
knn_classifier = joblib.load('/home/admin/.local/lib/python3.7/site-packages/KNN-Fall-Detection-main/KNN-Fall-Detection-main/Model/KeypointClassifier.joblib')

# Configure MediaPipe's Pose module
pose_visualizer = mp.solutions.drawing_utils
landmark_styles = mp.solutions.drawing_styles
pose_tracker = mp.solutions.pose

# Define the keypoints used for prediction
selected_keypoints = [
    "nose_x", "nose_y", "nose_z",
    "left_eye_x", "left_eye_y", "left_eye_z",
    "right_eye_x", "right_eye_y", "right_eye_z",
    "left_shoulder_x", "left_shoulder_y", "left_shoulder_z",
    "right_shoulder_x", "right_shoulder_y", "right_shoulder_z",
    "left_hip_x", "left_hip_y", "left_hip_z",
    "right_hip_x", "right_hip_y", "right_hip_z"
]

print(len(selected_keypoints))
keypoint_buffer = []

# Initialize video input from a camera
video_input = cv2.VideoCapture(0)
with pose_tracker.Pose(
        static_image_mode=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose_estimator:
    while video_input.isOpened():
        # Capture frames from the camera
        success, frame = video_input.read()
        if not success:
            print("Ignoring empty frame...")
            continue

        # Process the frame to extract pose keypoints
        frame.flags.writeable = False
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pose_results = pose_estimator.process(rgb_frame)

        if pose_results.pose_landmarks:
            for landmark in pose_results.pose_landmarks.landmark:
                keypoint_buffer.extend([landmark.x, landmark.y, landmark.z])

            num_frames = len(keypoint_buffer) // len(selected_keypoints)
            reshaped_keypoints = np.array(keypoint_buffer).reshape(num_frames, len(selected_keypoints))
            predictions = knn_classifier.predict(reshaped_keypoints)
            keypoint_buffer.clear()

            print(predictions)
            label = "Fall" if predictions[0] == 0 else "Normal"
            cv2.putText(frame, label, (100, 160), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 2)

        # Visualize pose annotations
        frame.flags.writeable = True
        annotated_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
        pose_visualizer.draw_landmarks(
            annotated_frame,
            pose_results.pose_landmarks,
            pose_tracker.POSE_CONNECTIONS,
            landmark_drawing_spec=landmark_styles.get_default_pose_landmarks_style()
        )

        current_frame_time = time.time()
        fps = 1 / (current_frame_time - time.time())
        cv2.putText(annotated_frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 196, 255), 2)

        cv2.imshow('Pose Detection Viewer', annotated_frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
            break

video_input.release()
