import cv2

def detect_motion(prev_frame, curr_frame, threshold=5000):
    if prev_frame is None:
        return True

    diff = cv2.absdiff(prev_frame, curr_frame)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    motion_score = thresh.sum()

    return motion_score > threshold
