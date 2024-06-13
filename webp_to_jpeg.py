import os
from tkinter import Tk, Label, Button, filedialog, Frame, BOTH, LEFT, RIGHT
from PIL import Image
import tkinter.font as font

def convert_webp_to_jpeg(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".webp"):
            webp_path = os.path.join(input_dir, filename)
            jpeg_filename = os.path.splitext(filename)[0] + ".jpeg"
            jpeg_path = os.path.join(output_dir, jpeg_filename)
            
            with Image.open(webp_path) as img:
                img = img.convert("RGB")
                img.save(jpeg_path, "JPEG")
    
    status_label.config(text="Conversion completed!", fg="green")

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
        convert_webp_to_jpeg(input_dir, output_dir)
    else:
        status_label.config(text="Please select both input and output directories.", fg="red")

root = Tk()
root.title("WEBP to JPEG Converter")
root.geometry("400x250")

# Set the Roboto font
roboto_font = font.Font(family="Roboto", size=12)
roboto_font_bold = font.Font(family="Roboto", size=16, weight="bold")

# Set background color
bg_color = root.cget('bg')

title_label = Label(root, text="WEBP to JPEG Converter", font=roboto_font_bold, bg=bg_color)
title_label.pack(pady=20)

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

convert_button = Button(root, text="Start Conversion", command=start_conversion, font=roboto_font, bg="lightgray")
convert_button.pack(pady=20)

status_label = Label(root, text="", font=roboto_font, bg=bg_color)
status_label.pack(pady=5)

root.mainloop()
