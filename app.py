import cv2
import tkinter as tk
from PIL import Image, ImageTk

from face_auth.recognizer import verify_user
from utils.liveness import is_live

cap = cv2.VideoCapture(0)

verify_count = 0
VERIFY_THRESHOLD = 3
recognized_user = None
frame_count = 0


def on_close():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()


def video_loop():
    global verify_count, recognized_user, frame_count

    ret, frame = cap.read()
    if not ret:
        return

    frame_count += 1

    if not is_live(frame):
        status_label.config(text="Spoof detected!")
    else:
        if frame_count % 5 == 0:  # optimize DeepFace calls
            user = verify_user(frame)

            if user != "Unknown":
                verify_count += 1
                status_label.config(text=f"{user} ({verify_count}/3)")

                if verify_count >= VERIFY_THRESHOLD:
                    recognized_user = user
                    status_label.config(text=f"Welcome {user} ✅")
            else:
                verify_count = 0
                status_label.config(text="Not recognized")

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    root.after(10, video_loop)


# GUI
root = tk.Tk()
root.title("Face Authentication System")

video_label = tk.Label(root)
video_label.pack()

status_label = tk.Label(root, text="Starting...", font=("Arial", 14))
status_label.pack()

root.protocol("WM_DELETE_WINDOW", on_close)
root.after(10, video_loop)

root.mainloop()
