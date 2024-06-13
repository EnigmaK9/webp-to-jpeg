from tkinter import Tk, Label

def open_about():
    about_window = Tk()
    about_window.title("About")
    about_window.geometry("300x200")
    roboto_font = ("Roboto", 12)  # Font family and size
    about_label = Label(about_window, text="WEBP to JPEG Converter\nVersion 1.0\nDeveloped by EnigmaK9\n© 2024", font=roboto_font, justify="center")
    about_label.pack(expand=True)
    about_window.mainloop()
