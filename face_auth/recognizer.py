from deepface import DeepFace
from face_auth.database import known_users
import cv2

DISTANCE_THRESHOLD = 0.4

def preprocess(face):
    return cv2.resize(face, (224, 224))

def verify_user(face_region):
    face_region = preprocess(face_region)

    for name, path in known_users.items():
        try:
            result = DeepFace.verify(face_region, path, enforce_detection=False)

            if result["verified"] and result["distance"] < DISTANCE_THRESHOLD:
                return name

        except Exception:
            continue

    return "Unknown"
