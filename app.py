import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

from face_auth.camera import detect_faces
from face_auth.recognizer import verify_face
from utils.security import AuthState, max_attempts

reference_img_path = "assets/my_face1.jpg"

cap = cv2.VideoCapture(0)

state = AuthState()

# ---------------- UI FUNCTIONS ----------------

def show_welcome():
    video_label.pack_forget()
    status_label.pack_forget()

    tk.Label(root, text="✅ Welcome!", font=("Helvetica", 24), fg="green").pack(pady=50)

def fallback_login():
    messagebox.showwarning("Login Failed", "Switching to password login.")
    root.destroy()
    cap.release()

# ---------------- MAIN LOOP ----------------

def video_loop():
    if state.authenticated:
        return

    ret, frame = cap.read()
    if not ret:
        return

    faces = detect_faces(frame)

    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]

        verified, dist = verify_face(face_region, reference_img_path)

        if verified:
            state.increment()
            status_label.config(text=f"Verified {state.verify_count}/3")

            if state.success():
                state.authenticated = True
                show_welcome()
                return
        else:
            state.reset()
            status_label.config(text="Not recognized")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Show frame
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    state.attempts += 1
    if state.attempts >= max_attempts:
        fallback_login()
        return

    root.after(10, video_loop)

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Face-ID Login")

video_label = tk.Label(root)
video_label.pack()

status_label = tk.Label(root, text="Starting...", font=("Helvetica", 14))
status_label.pack()

root.after(100, video_loop)
root.mainloop()
