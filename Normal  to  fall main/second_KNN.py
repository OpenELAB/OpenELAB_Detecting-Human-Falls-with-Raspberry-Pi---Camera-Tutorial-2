import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN

# Load datasets for normal and fall keypoints
normal_keypoints = pd.read_csv("/home/admin/.local/lib/python3.7/site-packages/KNN-Fall-Detection-main/KNN-Fall-Detection-main/2_Normal.csv")
fall_keypoints = pd.read_csv("/home/admin/.local/lib/python3.7/site-packages/KNN-Fall-Detection-main/KNN-Fall-Detection-main/1_fall.csv")

print(normal_keypoints.shape)
print(fall_keypoints.shape)

# Combine the datasets into a single DataFrame
combined_keypoints = pd.concat([normal_keypoints, fall_keypoints])
print(combined_keypoints)

# Separate the features and labels from the data
features = combined_keypoints.iloc[:, 1:]
labels = combined_keypoints.iloc[:, 0]

print(features.values)
print(labels.values)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features.values, labels.values, test_size=0.3, random_state=0)

print(X_train.shape)
print(y_train.shape)

# Train a K-Nearest Neighbors (KNN) classifier
knn_classifier = KNN(n_neighbors=3, algorithm='auto')
knn_classifier.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(knn_classifier, "/home/admin/.local/lib/python3.7/site-packages/KNN-Fall-Detection-main/KNN-Fall-Detection-main/Model/KeypointClassifier.joblib")
