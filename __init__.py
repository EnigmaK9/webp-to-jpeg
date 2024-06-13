# __init__.py

# Import key functions and classes to make them available directly from the package
from .gui import create_gui
from .converter import convert_webp_to_jpeg
from .utils import (
    create_directory_if_not_exists,
    get_image_files_from_directory,
    convert_image_to_jpeg
)

# Define what is available to import with a wildcard import (e.g., from package import *)
__all__ = [
    "create_gui",
    "convert_webp_to_jpeg",
    "create_directory_if_not_exists",
    "get_image_files_from_directory",
    "convert_image_to_jpeg"
]
