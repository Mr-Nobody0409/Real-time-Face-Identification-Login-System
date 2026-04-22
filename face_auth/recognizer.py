from deepface import DeepFace
from face_auth.database import known_users

distance_threshold = 0.4

def verify_against_db(face_region):
    for name, path in known_users.items():
        result = DeepFace.verify(face_region, path, enforce_detection=False)

        if result["verified"] and result["distance"] < distance_threshold:
            return name, result["distance"]

    return None, None
