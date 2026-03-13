import os
import customtkinter as ctk
import tkinter as tk

from ruldani_visual_programming.utils.pages import pages
from ruldani_visual_programming.utils.models import models
from ruldani_visual_programming.utils.presenters import presenters

import tkinter as tk
import ruldani_visual_programming.utils.color_manager as cm

from ruldani_visual_programming.utils.models.button_config import Button, SubButton

# Define colors
CYAN_PALLETE = cm.CYAN_PALLETE
ORANGE_PALLETE = cm.ORANGE_PALLETE
YELLOW_PALLETE = cm.ORANGE_PALLETE
LIGHT_GREEN_PALLETE = cm.LIGHT_GREEN_PALLETE    

# non pallete colors
SECONDARY_COLOR = cm.SECONDARY_COLOR
BACKGROUND_COLOR = cm.BACKGROUND_COLOR
TEXT_COLOR = cm.TEXT_COLOR
DARK_COLOR = cm.DARK_COLOR

# set appearance dark mode
ctk.set_appearance_mode("dark")

# Define Image
LOGO_IMAGE = "sub_home.png"

# Define Font
FONT = "Consolas"
PATH = "/code_from_scratch.py"

class visual_programming():
    
    def __init__(self):
        # make view
        view = pages()
        
        confg:str = self.read_file_to_string(PATH)
        # make model
        model = models(path_configuration=confg)

        # make presenter
        presenter = presenters(view=view, model=model)

        # make pages.preseter = presenter
        view.set_presenter(presenter=presenter)
        view.run()
        
        view.update()
        

        # run pages
        view.mainloop()

    def read_file_to_string(self, file_path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        try:
            with open(f"{base_dir}{file_path}", 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' tidak ditemukan")
            return None
        except Exception as e:
            print(f"Error membaca file: {e}")
            return None
    
if __name__ == "__main__":
    app = visual_programming()
