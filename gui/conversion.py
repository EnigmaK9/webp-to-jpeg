from converter import convert_webp_to_jpeg

def start_conversion(input_label, output_label, quality_entry, status_label):
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
