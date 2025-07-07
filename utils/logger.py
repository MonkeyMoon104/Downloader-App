import customtkinter as ctk

class Logger:
    def __init__(self, parent):
        self.output_box = ctk.CTkTextbox(
            parent,
            height=250,
            width=500,  
            corner_radius=15,
            fg_color="#111111",
            text_color="#e0e0e0",
            font=("Consolas", 14),
            wrap="word"
        )
        self.output_box.pack(pady=20)
        self.output_box.configure(state="disabled")

    def log(self, text):
        self.output_box.configure(state="normal")
        self.output_box.insert("end", f"{text}\n")
        self.output_box.see("end")
        self.output_box.configure(state="disabled")
