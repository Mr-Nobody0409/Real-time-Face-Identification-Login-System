from deepface import DeepFace

distance_threshold = 0.4

def verify_face(face_region, reference_img_path):
    try:
        result = DeepFace.verify(
            face_region,
            reference_img_path,
            enforce_detection=False
        )

        if result["verified"] and result["distance"] < distance_threshold:
            return True, result["distance"]
        return False, result["distance"]

    except Exception as e:
        print(f"DeepFace Error: {e}")
        return False, None
