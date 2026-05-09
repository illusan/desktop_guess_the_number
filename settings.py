import customtkinter as ctk

def settings_frame(settings):
    tab = ctk.CTkFrame(settings)

    settings.add(tab, text="Settings")

    def switch_event():
        if switch_var.get() == "on":
            ctk.set_appearance_mode("dark")
            text_theme.configure(text="Current theme: Dark")
        else:
            ctk.set_appearance_mode("light")
            text_theme.configure(text="Current theme: Light")
    

    switch_var = ctk.StringVar(value="on")

    text_theme = ctk.CTkLabel(tab, text="Current theme: Dark", font=("Arial", 16), )
    text_theme.pack(pady=(20, 0))

    switch = ctk.CTkSwitch(tab, text="toggle theme", command=switch_event, variable=switch_var, onvalue="on", offvalue="off")
    switch.pack()

    return tab