import os
from PIL import Image
import customtkinter as ctk
import tkinter as tk
import random
import pyperclip
from ruldani_visual_programming.utils import interpreter_code, nodeberzier, highlight, image
from ruldani_visual_programming.utils.pages.organism import ribbon, sidebar, content, settings, preferences
from ruldani_visual_programming.utils.pages.atomic import button
import tkinter as tk
import ruldani_visual_programming.utils.color_manager as cm

from ruldani_visual_programming.utils import Button, SubButton

# Define your base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

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

class visual_programming(tk.Tk):
    
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.make_window([1440, 720])

    def make_window(self, geometry:list[int]) -> None:

        width = geometry[0]
        height = geometry[1]

        self.geometry(f"{width}x{height}")
        self.title("Ruldani - Visual Programming")
        
        # Configure columns and rows to allow resizing
        self.grid_rowconfigure(0, weight=1)

        # configure workspace grid configure
        self.grid_columnconfigure(0, weight= 0)
        self.grid_columnconfigure(1, weight= 1)
        
            
        # make 2 panel : panel settings and main panel
        main_panel = self.main_panel()
        setting = settings(self)

        # make workspace and menubar on main panel
        workspace = self.workspace_panel(master=main_panel)
        menubar = ribbon(master=main_panel)
        
        # workspace panel
        sidebars = sidebar(master=workspace)
        contentz = content(master=workspace)
        preferencez = preferences(master=workspace)
        

    # make workspace panel
    def workspace_panel(self, master):
        workspace = ctk.CTkFrame(master=master, corner_radius=0)
        workspace.grid(row=1, column=1, sticky="nsew")
        workspace.grid_columnconfigure(0, weight=0)
        workspace.grid_columnconfigure(1, weight=1)
        workspace.grid_columnconfigure(2, weight=0)
        workspace.grid_rowconfigure(0, weight=1)

        return workspace

    def main_panel(self):
        main = ctk.CTkFrame(self, corner_radius=0)
        main.grid(row=0, column=1, sticky="nsew")
        main.grid_columnconfigure(0, weight=0)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(1, weight=1)
        return main
    
if __name__ == "__main__":
    app = visual_programming()
    app.mainloop()
