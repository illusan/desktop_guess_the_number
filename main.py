import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Main")
window.geometry("400x400")
window.configure(bg="#505D7A")

text = tk.Label(window, text="idk")
text.pack(pady=20)

button = tk.Button(window, text="button")
button.pack()

scndscreen = ttk.Notebook(window)
scndscreen.pack(expand=True, fill="both", pady=10, padx=10)

frame1 = ttk.Frame(scndscreen)
frame2 = ttk.Frame(scndscreen)

scndscreen.add(frame1, text="Main")
scndscreen.add(frame2, text="Settings")



window.mainloop()