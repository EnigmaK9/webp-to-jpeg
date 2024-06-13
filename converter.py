import os
from utils import create_directory_if_not_exists, get_image_files_from_directory, convert_image_to_jpeg

def convert_webp_to_jpeg(input_dir, output_dir, quality=85):
    create_directory_if_not_exists(output_dir)
    
    image_files = get_image_files_from_directory(input_dir, extensions=['.webp'])
    
    for webp_path in image_files:
        jpeg_filename = os.path.splitext(os.path.basename(webp_path))[0] + ".jpeg"
        jpeg_path = os.path.join(output_dir, jpeg_filename)
        
        convert_image_to_jpeg(webp_path, jpeg_path, quality)
    
    return "Conversion completed!"

