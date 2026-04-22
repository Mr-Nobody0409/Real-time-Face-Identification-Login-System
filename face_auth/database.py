import os

DATASET_PATH = "dataset/train"

known_users = {}

for file in os.listdir(DATASET_PATH):
    if file.endswith(".jpg"):
        name = file.split(".")[0]
        known_users[name] = os.path.join(DATASET_PATH, file)
