from deepface import DeepFace
from face_auth.database import known_users

def verify_user(face_region):
    for name, path in known_users.items():
        result = DeepFace.verify(face_region, path, enforce_detection=False)

        if result["verified"] and result["distance"] < 0.4:
            return name

    return "Unknown"
