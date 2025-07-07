import os
import zipfile
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
from data.config import FFMPEG_PATH

def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), folder_path))

def download_song(title, output_folder):
    search = VideosSearch(title, limit=1)
    result = search.result()["result"]
    if not result:
        raise ValueError(f"Nessun risultato trovato per: {title}")
    url = result[0]["link"]

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'ffmpeg_location': FFMPEG_PATH,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
