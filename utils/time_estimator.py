import time

class TimeEstimator:
    def __init__(self, app):
        self.app = app

    def update(self):
        if not self.app.download_in_progress or self.app.total_songs == 0:
            self.app.time_left_label.configure(text="Tempo stimato rimanente: --:--")
            return

        if self.app.completed_songs == 0:
            self.app.time_left_label.configure(text="Tempo stimato rimanente: calcolo in corso...")
        else:
            elapsed = time.time() - self.app.download_start_time
            avg = elapsed / self.app.completed_songs
            remaining = self.app.total_songs - self.app.completed_songs
            mins, secs = divmod(int(avg * remaining), 60)
            self.app.time_left_label.configure(text=f"Tempo stimato rimanente: {mins:02d}:{secs:02d}")

        if self.app.download_in_progress:
            self.app.after(500, self.update)
