from googleapiclient.discovery import build as google_build
import simpleaudio as sa
import dotenv as denv
import os 

denv.load_dotenv()
YOUTUBE_KEY = os.getenv("YOUTUBE_KEY")

print("API KEY: ", YOUTUBE_KEY)


