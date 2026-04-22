import hashlib

def hash_face_id(face_id: str):
    return hashlib.sha256(face_id.encode()).hexdigest()
