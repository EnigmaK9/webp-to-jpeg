import os
from PIL import Image

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
    
    return "Conversion completed!"
