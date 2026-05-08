import tkinter as tk

window = tk.Tk()

window.title("Main")
window.geometry("400x400")



button = tk.Button(window, text="button")
button.pack()

window.mainloop()