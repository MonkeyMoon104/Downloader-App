from dotenv import load_dotenv
import os

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
FFMPEG_PATH = os.getenv("FFMPEG_PATH")
LIST_FILE = os.getenv("LIST_FILE")
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER")
