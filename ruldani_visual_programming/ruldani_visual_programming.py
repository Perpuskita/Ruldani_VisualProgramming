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

# Define buttons and sub-buttons
buttons = [
    Button("Input System", "home.png", [
        # sub button folder
        SubButton("folder",
                    "folder.png",
                    LIGHT_GREEN_PALLETE),
        # sub button gdrive
        SubButton("gdrive folder",
                    "gdrive.png",
                    LIGHT_GREEN_PALLETE)
    ]),
    Button("Konsep Pendahuluan", "cpm1.png", [
        # sub button pembentukan citra
        SubButton("pembentukan citra",
                    "pembentukan citra.png",
                    CYAN_PALLETE),
    ]),
    Button("Pengolahan\nCitra digital", "cpm2.png", [
        # sub button analisa binner
        SubButton("analisa biner",
                    "analisa_citra_biner.png",
                    YELLOW_PALLETE),
        # sub button analisa abu
        SubButton("analisa abu",
                    "analisa_citra_abu.png",
                    YELLOW_PALLETE),
        # sub button transformasi fourier
        SubButton("transformasi fourier",
                    "transformasi_fourier.png",
                    YELLOW_PALLETE)
    ]),
    Button("Klasifikasi dan        \n Pengenalan Object", "cpm3.png", [
        # sub button deteksi tepi
        SubButton("deteksi tepi",
                    "deteksi_tepi.png",
                    ORANGE_PALLETE),
        # sub button ekstasi fitur
        SubButton("ekstraksi_fitur",
                    "ekstraksi_fitur.png",
                    ORANGE_PALLETE)
    ])
]

class visual_programming():
    
    def __init__(self):
        # make view
        view = pages()
        
        # make model
        model = models(buttons=buttons)

        # make presenter
        presenter = presenters(view=view, model=model)

        # make pages.preseter = presenter
        view.set_presenter(presenter=presenter)
        view.run()
        
        # run pages
        view.mainloop()

    
if __name__ == "__main__":
    app = visual_programming()
