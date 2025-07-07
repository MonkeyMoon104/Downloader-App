import customtkinter as ctk

def create_labels(app):
    label = ctk.CTkLabel(app, text="Seleziona la modalità di caricamento", font=("Helvetica", 24, "bold"))
    label.pack(pady=25)
    return label

def create_buttons(parent, app_instance):
    btn_youtube = ctk.CTkButton(parent, text="📂 Carica da file", command=app_instance.load_youtube, width=240, height=50, fg_color="#1f6aa5", hover_color="#145374", corner_radius=12)
    btn_youtube.pack(pady=12)

    btn_spotify = ctk.CTkButton(parent, text="🎵 Carica da Spotify", command=app_instance.load_spotify, width=240, height=50, fg_color="#1f6aa5", hover_color="#145374", corner_radius=12)
    btn_spotify.pack(pady=12)

    btn_start = ctk.CTkButton(parent, text="⬇️ Avvia Download", command=app_instance.start_download, state="disabled", width=240, height=50, fg_color="#f39c12", hover_color="#d68910", corner_radius=12)
    btn_start.pack(pady=15)

    return btn_youtube, btn_spotify, btn_start

def create_progress_elements(app):
    progress = ctk.CTkProgressBar(app, width=460, height=20, progress_color="#0f9d58")
    progress.set(0)
    progress.pack(pady=25)

    time_left_label = ctk.CTkLabel(app, text="Tempo stimato rimanente: --:--", font=("Helvetica", 14))
    time_left_label.pack(pady=5)

    return progress, time_left_label
