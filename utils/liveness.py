import cv2

prev_frame = None

def is_live(frame):
    global prev_frame

    if prev_frame is None:
        prev_frame = frame
        return True

    diff = cv2.absdiff(prev_frame, frame)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    motion_score = gray.sum()
    prev_frame = frame

    return motion_score > 5000
