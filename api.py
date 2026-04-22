from fastapi import FastAPI
import time

from face_auth.recognizer import verify_against_db

app = FastAPI()

@app.post("/login")
def login():
    start = time.time()

    # (simulate frame input for now)
    # integrate camera later if needed

    user, dist = verify_against_db("sample_frame")

    latency = (time.time() - start) * 1000  # ms

    return {
        "user": user,
        "latency_ms": latency
    }
