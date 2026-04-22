import os

DATASET_PATH = "dataset/train"

def load_users():
    users = {}
    if not os.path.exists(DATASET_PATH):
        return users

    for file in os.listdir(DATASET_PATH):
        if file.endswith(".jpg"):
            name = file.split(".")[0]
            users[name] = os.path.join(DATASET_PATH, file)

    return users

known_users = load_users()
