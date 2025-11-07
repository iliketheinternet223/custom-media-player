import os
import importlib
import sys

REQUIRED_MODULES = ["googleapiclient.discovery", "simpleaudio", "dotenv", "tqdm"]

for module in REQUIRED_MODULES:
    try:
        importlib.import_module(module)
    except ImportError:
        print(f"Missing module: {module}")
        choice = input("Would you like to install missing modules? (y/n): ").strip().lower()
        if choice == "y":
            os.system("pip install -r requirements.txt")
            break
        else:
            sys.exit("Please install the required modules and try again.")

from googleapiclient.discovery import build as google_build
import simpleaudio as sa
import dotenv as denv
import tqdm

print("All modules imported successfully.")

denv.load_dotenv()
YOUTUBE_KEY = os.getenv("YOUTUBE_KEY")

if YOUTUBE_KEY is None:
    raise ValueError("YOUTUBE_KEY not found in environment variables. Please refer to the README for setup instructions.")

yAPI = google_build("youtube", "v3", developerKey=YOUTUBE_KEY)
print("YouTube API client initialized successfully.")

