import customtkinter as ctk
from tkinter import ttk
import settings
import random

ctk.set_appearance_mode("dark")

random_number = random.randint(1,100)

def check_number():
    user_number = textbox.get()

    if not user_number.isdigit():
        text.configure(text="Type only numbers!", text_color="red")
        return
    
    number = int(user_number)

    if number < random_number:
        text.configure(text="Your number is too small!", text_color="blue")
    elif number > random_number:
        text.configure(text="Your number is too big!", text_color="blue")
    else:
        text.configure(text="Congrats! You guessed it!", text_color="green")

# -----

window = ctk.CTk()

window.title("Guess the number!")
window.geometry("600x450")

window.resizable(False, False)


scndscreen = ttk.Notebook(window)
scndscreen.pack(expand=True, fill="both")

frame1 = ctk.CTkFrame(scndscreen)
scndscreen.add(frame1, text="Main")

text = ctk.CTkLabel(frame1, text="Guess the number!", font=("Arial", 16))
text.pack(pady=(50, 0))

text2 = ctk.CTkLabel(frame1, text="(Generated number is between 1-100)")
text2.pack(pady=(0, 10))

textbox = ctk.CTkEntry(frame1)
textbox.pack()

button = ctk.CTkButton(frame1, text="Guess", command=check_number)
button.pack(pady=20)

frame2 = settings.settings_frame(scndscreen)

# changing tab problem solve (problem solved by AI)
def refresh_tab(event):
    window.update_idletasks()

scndscreen.bind("<<NotebookTabChanged>>", refresh_tab)
# -----

window.mainloop()