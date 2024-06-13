# WEBP to JPEG Converter

## Description

This project is a simple graphical user interface (GUI) application that converts images from WEBP format to JPEG format. It allows users to select the input and output directories and set the JPEG quality. The application is built using Python and the `tkinter` library for the GUI, and `Pillow` for image processing.

## Features

- Select input and output directories for conversion
- Set JPEG quality (1-100)
- Simple and user-friendly GUI
- About window with application details

## Requirements

- Python 3.x
- Pillow library
- tkinter library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/webp-to-jpeg.git
   cd webp-to-jpeg
   ```

2. **Create a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install pillow
   ```

4. **Ensure the font "Roboto" is installed on your system.**

   - You can download it from [Google Fonts](https://fonts.google.com/specimen/Roboto).

## Usage

1. **Run the application:**

   ```sh
   python main.py
   ```

2. **Select the input directory:**

   - Click the "Select" button next to "Input Directory" and choose the directory containing WEBP images.

3. **Select the output directory:**

   - Click the "Select" button next to "Output Directory" and choose the directory where the converted JPEG images will be saved.

4. **Set the JPEG quality:**

   - Enter a value between 1 and 100 in the "JPEG Quality" field. The default is 85.

5. **Start the conversion:**

   - Click the "Start Conversion" button. The status will be displayed at the bottom of the window.

6. **View application details:**
   - Click the "About" button to view additional information about the application.

## Files

- `main.py`: The entry point of the application.
- `converter.py`: Contains the logic for converting WEBP images to JPEG.
- `gui.py`: Contains the GUI logic and layout.
- `utils.py`: Currently empty, can be used for utility functions.
- `README.md`: Project documentation.

## Creating an Executable

To create a standalone executable for Windows, you can use `PyInstaller`.

1. **Install PyInstaller:**

   ```sh
   pip install pyinstaller
   ```

2. **Create the executable:**

   ```sh
   pyinstaller --onefile --noconsole main.py
   ```

3. **The executable will be located in the `dist` directory.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Developed by Enigm.

## Acknowledgements

- [Pillow](https://python-pillow.org/) - The Python Imaging Library
- [tkinter](https://docs.python.org/3/library/tkinter.html) - The GUI toolkit for Python
- [Roboto Font](https://fonts.google.com/specimen/Roboto) - Font used in the application
