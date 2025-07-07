import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from io import BytesIO
import requests
from utils.spotify_utils import get_spotify_titles


def create_spotify_popup(app):
    def on_confirm():
        url = url_entry.get()
        if not url:
            popup.destroy()
            return
        try:
            data = get_spotify_titles(url)

            info_label.configure(text=(
                f"🎷 Playlist: {data['name']}\n"
                f"👤 Creatore: {data['owner']}\n"
                f"🎼 Brani totali: {data['count']}\n"
                f"📃 {data['description'][:200]}{'...' if len(data['description']) > 200 else ''}"
            ))

            if data.get("cover_url"):
                response = requests.get(data["cover_url"])
                img = Image.open(BytesIO(response.content)).resize((220, 220))
                cover_img = ctk.CTkImage(dark_image=img, size=(220, 220))
                cover_label.configure(image=cover_img, text="")
                cover_label.image = cover_img

            def start_download_action():
                app.titles = data["titles"]
                app.btn_start.configure(state="normal")
                app.logger.log(f"✅ Playlist '{data['name']}' caricata.")
                popup.destroy()

            def cancel_action():
                popup.destroy()

            confirm_btn.configure(command=start_download_action)
            cancel_btn.configure(command=cancel_action)

        except Exception as e:
            messagebox.showerror("Errore Spotify", str(e))
            popup.destroy()

    popup = ctk.CTkToplevel(app)
    popup.title("Inserisci URL Playlist Spotify")
    popup.geometry("420x580")

    url_label = ctk.CTkLabel(popup, text="URL Playlist Spotify:", font=("Helvetica", 14, "bold"))
    url_label.pack(pady=(20, 5))

    url_entry = ctk.CTkEntry(popup, width=380)
    url_entry.pack(pady=5)

    go_btn = ctk.CTkButton(popup, text="Carica playlist", fg_color="#1f6aa5", hover_color="#145374", command=on_confirm)
    go_btn.pack(pady=10)

    info_label = ctk.CTkLabel(popup, text="", justify="left", wraplength=380)
    info_label.pack(pady=15)

    cover_label = ctk.CTkLabel(popup, text="", corner_radius=15, fg_color="#222222", width=220, height=220)
    cover_label.pack(pady=10)

    confirm_btn = ctk.CTkButton(popup, text="Scarica", fg_color="#27ae60", hover_color="#219150")
    confirm_btn.pack(pady=5)

    cancel_btn = ctk.CTkButton(popup, text="Annulla", fg_color="#c0392b", hover_color="#922b21")
    cancel_btn.pack(pady=5)
