def animate_button(app):
    if not app.anim_running:
        app.btn_start.configure(text="⬇️ Avvia Download")
        return
    app.anim_index = (app.anim_index + 1) % len(["⬇️", "🔽", "⏬", "⬇️"])
    new_text = f"{['⬇️', '🔽', '⏬', '⬇️'][app.anim_index]} Download in corso..."
    app.btn_start.configure(text=new_text)
    app.after(600, lambda: animate_button(app))
