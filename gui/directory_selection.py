from tkinter import filedialog

def select_input_directory(label):
    input_dir = filedialog.askdirectory()
    label.config(text=f"Input Directory: {input_dir}")
    return input_dir

def select_output_directory(label):
    output_dir = filedialog.askdirectory()
    label.config(text=f"Output Directory: {output_dir}")
    return output_dir
