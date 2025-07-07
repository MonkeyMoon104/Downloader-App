import os
import sys
from dotenv import load_dotenv
from ui.app import App

DEFAULT_ENV_CONTENT = """\
SPOTIPY_CLIENT_ID=
SPOTIPY_CLIENT_SECRET=
FFMPEG_PATH=C:/ffmpeg/bin/ffmpeg.exe
LIST_FILE=files/listsong.txt
OUTPUT_FOLDER=downloaded_songs
"""

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def ensure_env_file():
    base_dir = get_base_dir()
    env_path = os.path.join(base_dir, ".env")

    if not os.path.exists(env_path):
        with open(env_path, "w") as f:
            f.write(DEFAULT_ENV_CONTENT)
        print(f"File .env creato in {env_path}, modifica con le tue credenziali.")

def load_config():
    base_dir = get_base_dir()
    env_path = os.path.join(base_dir, ".env")
    load_dotenv(env_path)

if __name__ == "__main__":
    ensure_env_file()
    load_config()
    app = App()
    app.mainloop()
