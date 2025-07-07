import os
import threading
from utils.downloader import download_song, zip_folder

def run_download_thread(app, titles, output_folder):
    def _thread():
        os.makedirs(output_folder, exist_ok=True)
        app.after(0, lambda: app.logger.log("🚀 Inizio download sequenziale...\n"))

        for title in titles:
            app.after(0, lambda t=title: app.logger.log(f"🔄 Scaricando: {t}"))
            try:
                download_song(title, output_folder)
                app.after(0, lambda t=title: app.logger.log(f"✅ Completato: {t}"))
            except Exception as e:
                app.after(0, lambda t=title, e=e: app.logger.log(f"❌ Errore su '{t}': {e}"))
            app.completed_songs += 1
            progress_value = app.completed_songs / len(titles)
            app.after(0, lambda v=progress_value: app.progress.set(v))

        zip_folder(output_folder, f"{output_folder}.zip")
        app.after(0, lambda: app.logger.log("\n🎉 Tutti i download completati! Archivio ZIP creato."))
        app.after(0, lambda: setattr(app, "download_in_progress", False))
        app.after(0, lambda: setattr(app, "anim_running", False))
        app.after(0, app.finish_download_ui_update)

    threading.Thread(target=_thread, daemon=True).start()
