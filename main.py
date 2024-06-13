import sys
import os

# Add the current directory to the Python path to ensure modules can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui import create_gui

if __name__ == "__main__":
    create_gui()
