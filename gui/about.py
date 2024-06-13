from tkinter import Toplevel, Label, Frame, CENTER, BOTH
from tkinter.font import Font

def open_about():
    about_window = Toplevel()
    about_window.title("About")
    about_window.geometry("400x300")
    about_window.resizable(False, False)
    
    # Set fonts
    title_font = Font(family="Roboto", size=16, weight="bold")
    text_font = Font(family="Roboto", size=12)

    # Set colors
    bg_color = "#f0f0f0"
    fg_color = "#333333"
    highlight_color = "#ff6f61"
    
    # Set background color
    about_window.configure(bg=bg_color)
    
    # Create title frame
    title_frame = Frame(about_window, bg=highlight_color)
    title_frame.pack(fill=BOTH, padx=10, pady=(10, 0))
    
    title_label = Label(title_frame, text="About WEBP to JPEG Converter", font=title_font, bg=highlight_color, fg="white")
    title_label.pack(pady=10)

    # Create content frame
    content_frame = Frame(about_window, bg=bg_color)
    content_frame.pack(fill=BOTH, padx=10, pady=10)

    # Add content
    about_label = Label(content_frame, text="Version 1.0", font=text_font, bg=bg_color, fg=fg_color, justify=CENTER)
    about_label.pack(pady=(10, 5))
    
    developer_label = Label(content_frame, text="Developed by EnigmaK9", font=text_font, bg=bg_color, fg=fg_color, justify=CENTER)
    developer_label.pack(pady=5)
    
    copyright_label = Label(content_frame, text="© 2024", font=text_font, bg=bg_color, fg=fg_color, justify=CENTER)
    copyright_label.pack(pady=5)

    # Add icon (if you have an icon file, e.g., icon.png)
    # about_window.iconphoto(False, tk.PhotoImage(file='icon.png'))
    
    about_window.mainloop()
