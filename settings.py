import tkinter as tk

def settings_frame(settings):
    tab = tk.Frame(settings, bg="white")

    settings.add(tab, text="Settings")

    return tab