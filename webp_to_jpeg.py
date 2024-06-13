import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image

def convert_webp_to_jpeg(input_dir, output_dir):
    # Create the output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".webp"):
            # Full path to the input file
            webp_path = os.path.join(input_dir, filename)
            # Change the extension to .jpeg for the output file
            jpeg_filename = os.path.splitext(filename)[0] + ".jpeg"
            # Full path to the output file
            jpeg_path = os.path.join(output_dir, jpeg_filename)
            
            # Open the .webp file and convert it to .jpeg
            with Image.open(webp_path) as img:
                img = img.convert("RGB")
                img.save(jpeg_path, "JPEG")
    
    print("Conversion completed.")

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
        print("Please select both input and output directories.")

# Create the main window
root = Tk()
root.title("WEBP to JPEG Converter")

# Create and place the widgets
input_label = Label(root, text="Input Directory: ")
input_label.pack(pady=10)
input_button = Button(root, text="Select Input Directory", command=select_input_directory)
input_button.pack(pady=5)

output_label = Label(root, text="Output Directory: ")
output_label.pack(pady=10)
output_button = Button(root, text="Select Output Directory", command=select_output_directory)
output_button.pack(pady=5)

convert_button = Button(root, text="Start Conversion", command=start_conversion)
convert_button.pack(pady=20)

# Run the application
root.mainloop()
