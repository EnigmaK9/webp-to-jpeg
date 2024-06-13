from tkinter import Tk, Label, Button, Frame, BOTH, LEFT, RIGHT, BOTTOM, Entry
import tkinter.font as font
from .directory_selection import select_input_directory, select_output_directory
from .conversion import start_conversion
from .about import open_about

def create_gui():
    root = Tk()
    root.title("WEBP to JPEG Converter")
    root.geometry("500x400")

    # Set the Roboto font
    roboto_font = font.Font(family="Roboto", size=12)
    roboto_font_bold = font.Font(family="Roboto", size=16, weight="bold")

    # Set background color
    bg_color = root.cget('bg')

    title_label = Label(root, text="WEBP to JPEG Converter", font=roboto_font_bold, bg=bg_color)
    title_label.pack(pady=10)

    input_frame = Frame(root, bg=bg_color)
    input_frame.pack(fill=BOTH, padx=20, pady=5)

    input_label = Label(input_frame, text="Input Directory: ", font=roboto_font, bg=bg_color)
    input_label.pack(side=LEFT)
    input_button = Button(input_frame, text="Select", command=lambda: select_input_directory(input_label), font=roboto_font, bg="lightblue")
    input_button.pack(side=RIGHT)

    output_frame = Frame(root, bg=bg_color)
    output_frame.pack(fill=BOTH, padx=20, pady=5)

    output_label = Label(output_frame, text="Output Directory: ", font=roboto_font, bg=bg_color)
    output_label.pack(side=LEFT)
    output_button = Button(output_frame, text="Select", command=lambda: select_output_directory(output_label), font=roboto_font, bg="lightgreen")
    output_button.pack(side=RIGHT)

    quality_frame = Frame(root, bg=bg_color)
    quality_frame.pack(fill=BOTH, padx=20, pady=5)

    quality_label = Label(quality_frame, text="JPEG Quality (1-100): ", font=roboto_font, bg=bg_color)
    quality_label.pack(side=LEFT)
    quality_entry = Entry(quality_frame, font=roboto_font, width=5)
    quality_entry.insert(0, "85")
    quality_entry.pack(side=RIGHT)

    convert_button = Button(root, text="Start Conversion", command=lambda: start_conversion(input_label, output_label, quality_entry, status_label), font=roboto_font, bg="lightgray")
    convert_button.pack(pady=20)

    status_label = Label(root, text="", font=roboto_font, bg=bg_color)
    status_label.pack(pady=5)

    about_button = Button(root, text="About", command=open_about, font=roboto_font, bg="lightyellow")
    about_button.pack(side=BOTTOM, pady=10)

    root.mainloop()
