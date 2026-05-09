import tkinter as tk
from tkinter import ttk
import settings
import random

random_number = random.randint(1,100)

def check_number():
    user_number = textbox.get()

    if not user_number.isdigit():
        text.configure(text="Type only numbers!", bg="red")
        return
    
    number = int(user_number)

    if number < random_number:
        text.configure(text="Your number is too small!", fg="blue")
    elif number > random_number:
        text.configure(text="Your number is too big!", fg="blue")
    else:
        text.configure(text="Congrats! You guessed it!", fg="green")



window = tk.Tk()

window.title("Guess the number!")
window.geometry("800x600")
window.configure(bg="#505D7A")

scndscreen = ttk.Notebook(window)
scndscreen.pack(expand=True, fill="both")

frame1 = tk.Frame(scndscreen, bg="white")
scndscreen.add(frame1, text="Main")

text = tk.Label(frame1, text="Guess the number!", bg="white", font=("Arial", 16), fg="black")
text.pack(pady=20)

textbox = tk.Entry(frame1)
textbox.pack()

button = tk.Button(frame1, text="Guess", command=check_number)
button.pack(pady=20)

frame2 = settings.settings_frame(scndscreen)

window.mainloop()