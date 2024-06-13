from tkinter import Tk, Label, Button, filedialog, Frame, BOTH, LEFT, RIGHT, TOP, BOTTOM, Entry
import tkinter.font as font
from converter import convert_webp_to_jpeg

def create_gui():
    root = Tk()
    root.title("WEBP to JPEG Converter")
    root.geometry("500x400")

    # Set the Roboto font
    roboto_font = font.Font(family="Roboto", size=12)
    roboto_font_bold = font.Font(family="Roboto", size=16, weight="bold")

    # Set background color
    bg_color = root.cget('bg')

    def select_input_directory():
        input_dir = filedialog.askdirectory()
        input_label.config(text=f"Input Directory: {input_dir}")
        return input_dir

    def select_output_directory():
        output_dir = filedialog.askdirectory()
        output_label.config(text=f"Output Directory: {output_dir}")
        return output_dir

    def start_conversion():
        input_dir = input_label.cget("text").replace("Input Directory: ", "")
        output_dir = output_label.cget("text").replace("Output Directory: ", "")
        if input_dir and output_dir:
            try:
                quality = int(quality_entry.get())
                if quality < 1 or quality > 100:
                    raise ValueError
            except ValueError:
                status_label.config(text="Please enter a valid quality (1-100).", fg="red")
                return
            message = convert_webp_to_jpeg(input_dir, output_dir, quality)
            status_label.config(text=message, fg="green")
        else:
            status_label.config(text="Please select both input and output directories.", fg="red")

    def open_about():
        about_window = Tk()
        about_window.title("About")
        about_window.geometry("300x200")
        about_label = Label(about_window, text="WEBP to JPEG Converter\nVersion 1.0\nDeveloped by EnigmaK9\n© 2024", font=roboto_font, justify="center")
        about_label.pack(expand=True)
        about_window.mainloop()

    title_label = Label(root, text="WEBP to JPEG Converter", font=roboto_font_bold, bg=bg_color)
    title_label.pack(pady=10)

    input_frame = Frame(root, bg=bg_color)
    input_frame.pack(fill=BOTH, padx=20, pady=5)

    input_label = Label(input_frame, text="Input Directory: ", font=roboto_font, bg=bg_color)
    input_label.pack(side=LEFT)
    input_button = Button(input_frame, text="Select", command=select_input_directory, font=roboto_font, bg="lightblue")
    input_button.pack(side=RIGHT)

    output_frame = Frame(root, bg=bg_color)
    output_frame.pack(fill=BOTH, padx=20, pady=5)

    output_label = Label(output_frame, text="Output Directory: ", font=roboto_font, bg=bg_color)
    output_label.pack(side=LEFT)
    output_button = Button(output_frame, text="Select", command=select_output_directory, font=roboto_font, bg="lightgreen")
    output_button.pack(side=RIGHT)

    quality_frame = Frame(root, bg=bg_color)
    quality_frame.pack(fill=BOTH, padx=20, pady=5)

    quality_label = Label(quality_frame, text="JPEG Quality (1-100): ", font=roboto_font, bg=bg_color)
    quality_label.pack(side=LEFT)
    quality_entry = Entry(quality_frame, font=roboto_font, width=5)
    quality_entry.insert(0, "85")
    quality_entry.pack(side=RIGHT)

    convert_button = Button(root, text="Start Conversion", command=start_conversion, font=roboto_font, bg="lightgray")
    convert_button.pack(pady=20)

    status_label = Label(root, text="", font=roboto_font, bg=bg_color)
    status_label.pack(pady=5)

    about_button = Button(root, text="About", command=open_about, font=roboto_font, bg="lightyellow")
    about_button.pack(side=BOTTOM, pady=10)

    root.mainloop()
