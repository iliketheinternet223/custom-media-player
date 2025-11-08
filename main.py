import os
import importlib
import sys

REQUIRED_MODULES = ["googleapiclient.discovery", "simpleaudio", "dotenv", "tqdm", "yt_dlp"]
YOUTUBE_KEY = ""

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
import yt_dlp

print("All modules imported successfully.")

flogin = None

if os.path.exists(f"data/{os.getlogin()}.txt"):
    with open(f"data/{os.getlogin()}.txt", "r") as configfile:
        lines = configfile.readlines()
        flogin = lines[0].strip()
else:
    with open(f"data/{os.getlogin()}.txt", "w") as configfile:
        configfile.write("False")

if flogin == "False":
    with open(".env", "w") as envfile:
        envfile.write("YOUTUBE_KEY=")
        print("Please set your YOUTUBE_KEY in the .env file created. Refer to the README for setup instructions.")
        input("Press Enter after updating the .env file...")
        try:
            denv.load_dotenv()
            YOUTUBE_KEY = os.getenv("YOUTUBE_KEY")
            if not YOUTUBE_KEY:
                raise ValueError("YOUTUBE_KEY not set.")
        except ValueError as e:
            sys.exit(f"Error loading YOUTUBE_KEY: {e}")
        else:
            with open(f"data/{os.getlogin()}.txt", "w") as configfile:
                configfile.write("True")
elif flogin == "True":
    denv.load_dotenv()
    YOUTUBE_KEY = os.getenv("YOUTUBE_KEY")


yAPI = google_build("youtube", "v3", developerKey=YOUTUBE_KEY)
print("YouTube API client initialized successfully.")
print("================================")
print("Type playlist link")
i=input("> ")

ydl_opts = {
    'outtmpl': 'data/playlists/%(playlist_title)s/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'noplaylist': False,   # ensures full playlist is downloaded
    'quiet': True,
    'no_warnings': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore
    ydl.download([i])
print("Download completed successfully.")