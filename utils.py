import os
from PIL import Image

def create_directory_if_not_exists(directory):
    """
    Creates the specified directory if it does not already exist.
    
    Args:
    - directory (str): The path of the directory to create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_image_files_from_directory(directory, extensions=['.webp']):
    """
    Retrieves a list of image files from the specified directory with the given extensions.
    
    Args:
    - directory (str): The path of the directory to search.
    - extensions (list): A list of file extensions to include.
    
    Returns:
    - list: A list of file paths that match the specified extensions.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in extensions]

def convert_image_to_jpeg(image_path, output_path, quality=85):
    """
    Converts an image to JPEG format.
    
    Args:
    - image_path (str): The path of the input image.
    - output_path (str): The path where the output JPEG should be saved.
    - quality (int): The quality setting for the JPEG (1-100).
    """
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img.save(output_path, "JPEG", quality=quality)
