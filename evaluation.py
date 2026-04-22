import os
from face_auth.recognizer import verify_user
import cv2

TEST_PATH = "dataset/test"

def evaluate():
    correct = 0
    total = 0

    for file in os.listdir(TEST_PATH):
        if file.endswith(".jpg"):
            path = os.path.join(TEST_PATH, file)

            img = cv2.imread(path)

            predicted = verify_user(img)

            actual = file.split("_")[0]

            if predicted == actual:
                correct += 1

            total += 1

    accuracy = correct / total if total > 0 else 0

    print(f"Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    evaluate()
