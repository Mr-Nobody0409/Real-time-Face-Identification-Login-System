from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Face Auth API Running"}

@app.post("/login")
def login():
    start = time.time()

    # Dummy response (integrate camera if needed)
    user = "Demo_User"

    latency = (time.time() - start) * 1000

    return {
        "user": user,
        "latency_ms": latency
    }
