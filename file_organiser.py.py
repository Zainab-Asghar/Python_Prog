import os
import shutil
import time

# Path to your Downloads folder
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# File type → Folder mapping
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"]
}

def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        if os.path.isfile(file_path):
            for folder, extensions in FILE_TYPES.items():
                if filename.lower().endswith(tuple(extensions)):
                    target_folder = os.path.join(DOWNLOADS_FOLDER, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, target_folder)
                    break

# Run continuously
while True:
    organize_files()
    time.sleep(10)  # checks every 10 seconds
