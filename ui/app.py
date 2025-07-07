import customtkinter as ctk
from tkinter import messagebox
from ui.components import create_buttons, create_labels, create_progress_elements
from ui.spotify_popup import create_spotify_popup
from ui.animation import animate_button
from utils.logger import Logger
from utils.time_estimator import TimeEstimator
from utils.threading_utils import run_download_thread
from data.config import LIST_FILE, OUTPUT_FOLDER
from utils.downloader import download_song, zip_folder
import os
import shutil
import time

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🎧 Downloader")
        self.geometry("640x680")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.main_frame = ctk.CTkFrame(self.container)
        self.main_frame.pack(fill="both", expand=True)

        self.titles = []
        self.download_in_progress = False
        self.download_start_time = None
        self.completed_songs = 0
        self.total_songs = 0
        self.anim_running = False
        self.anim_index = 0

        self.label = create_labels(self.main_frame)
        self.btn_youtube, self.btn_spotify, self.btn_start = create_buttons(self.main_frame, self)
        self.progress, self.time_left_label = create_progress_elements(self.main_frame)
        self.logger = Logger(self.main_frame)

        self.time_estimator = TimeEstimator(self)


    def load_youtube(self):
        if not os.path.exists(LIST_FILE):
            messagebox.showerror("Errore", f"File non trovato: {LIST_FILE}")
            return
        with open(LIST_FILE, "r", encoding="utf-8") as f:
            self.titles = [line.strip() for line in f if line.strip()]
        self.logger.log(f"✅ Caricati {len(self.titles)} titoli dal file.")
        self.btn_start.configure(state="normal")
        self.img_label.configure(image="", text="")

    def load_spotify(self):
        create_spotify_popup(self)

    def start_download(self):
        if not self.titles:
            messagebox.showinfo("Info", "Nessuna canzone da scaricare.")
            return
        if self.download_in_progress:
            messagebox.showinfo("Info", "Download già in corso.")
            return

        self.download_in_progress = True
        self.btn_start.configure(state="disabled")
        self.progress.set(0)
        self.anim_running = True
        animate_button(self)

        self.download_start_time = time.time()
        self.completed_songs = 0
        self.total_songs = len(self.titles)

        self.time_estimator.update()
        run_download_thread(self, self.titles, OUTPUT_FOLDER)

    def finish_download_ui_update(self):
        try:
            if os.path.exists(OUTPUT_FOLDER):
                shutil.rmtree(OUTPUT_FOLDER)
                self.logger.log(f"🧹 Cartella temporanea '{OUTPUT_FOLDER}' rimossa.")
            else:
                self.logger.log(f"ℹ️ Cartella '{OUTPUT_FOLDER}' non trovata, nulla da rimuovere.")
        except Exception as e:
            self.logger.log(f"⚠️ Errore nella rimozione della cartella: {e}")

        self.btn_start.configure(state="normal")
        self.logger.log("✅ Interfaccia aggiornata dopo il download.")
