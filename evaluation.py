import os
import cv2
from face_auth.recognizer import verify_user

TEST_PATH = "dataset/test"

def evaluate():
    correct = 0
    total = 0

    for file in os.listdir(TEST_PATH):
        if file.endswith(".jpg"):
            path = os.path.join(TEST_PATH, file)

            img = cv2.imread(path)
            if img is None:
                continue

            predicted = verify_user(img)
            actual = file.split("_")[0]

            print(f"{file} → Predicted: {predicted}, Actual: {actual}")

            if predicted == actual:
                correct += 1

            total += 1

    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"\nAccuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    evaluate()
