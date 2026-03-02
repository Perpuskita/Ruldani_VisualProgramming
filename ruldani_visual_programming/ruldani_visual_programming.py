import os
from PIL import Image
import customtkinter as ctk
import tkinter as tk
import random
import pyperclip
from ruldani_visual_programming.utils import interpreter_code, nodeberzier, highlight, image
from ruldani_visual_programming.utils.pages import *
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
        main_panel = self.main_panel()

        # make workspace and workspace widget
        workspace = self.workspace_panel(master=main_panel)
        sidebars = sidebar(master=workspace)
        contentz = content(master=workspace)
        setting = self.setting_widget(workspace=self)
        preference = self.preference_widget(workspace=workspace)
        menubar = ribbon(master=main_panel)
        
        # make ribbon widget
        # ribbon = self.ribbon_widget(menubar=menubar)

        # make content setting
        setting_sidebar = self.setting_sidebar_widget(master=setting)
        
        # make content preference
        preferences_menu = self.preference_menu(master=preference)

        # make content of code
        # vsual = self.switch_content_widget(content)

        # make content of sidebar
        # content_sidebar =  self.sidebar_content(sidebar)

    def setting_sidebar_widget(self, master: ctk.CTkFrame):

        img: list[str] = ["thumbnail_bar.png","cpm1.png", "cpm2.png", "cpm3.png"]

        for i, image in enumerate(img):
            atomic = button(master=master, icon=image)
            if i == 0 :
                atomic.grid(row=i, column=0, pady= (3, 5), padx=(5, 5), sticky="n")

            else :
                atomic.grid(row=i, column=0, pady= (5, 5), padx=(5, 5), sticky="n")

        master.grid_rowconfigure(len(img), weight=1) 

        tes = button(master=master, icon="settings.png")
        tes.grid(row=len(img) + 1, column=0, pady = 5, padx = 0, sticky="ns" )
        return None

    # Create sidebar frame
    def setting_widget(self, workspace: ctk.CTkFrame) -> ctk.CTkFrame:
        setting = ctk.CTkFrame(workspace, width=40, corner_radius=0, fg_color=BACKGROUND_COLOR)
        setting.grid(row=0, column=0, sticky="ns")

        setting.grid_propagate(False)
        setting.grid_columnconfigure(3, weight=1)
        return setting

    def sidebar_widget(self, workspace: ctk.CTkFrame) -> ctk.CTkFrame:
        # Create sidebar frame
        sidebar = ctk.CTkFrame(workspace, width=200, corner_radius=0, fg_color=BACKGROUND_COLOR)
        sidebar.grid(row=0, column=0, sticky="nsw")

        # 1. Kunci lebar sidebar agar tidak berubah sesuai isi
        sidebar.grid_propagate(False)
        sidebar.grid_columnconfigure(0, weight=1)

        return sidebar

    def preference_menu(self, master) -> ctk.CTkEntry:
        tes = preference_text(master=master, text="nama node")
        tes.grid(row =1, column=0, sticky = "ew", padx = 20, pady=[20,0])
        result = preference(master=master)
        result.grid(row=2, column=0, padx=20, pady=10, sticky ="w")
        tes = preference_error(master=master, text="yahh error !")
        tes.grid(row =3, column=0, sticky = "ew", padx = 20)

        tes = preference_text(master=master, text="dropdown node")
        tes.grid(row =4, column=0, sticky = "ew", padx = 20, pady=[10,0])
        pilihan: list[str] = ["yus", "pos", "los"]
        ops = preference_dropdown(master=master, values=pilihan)
        ops.grid(row =5, column=0, sticky = "ew", padx = 20, pady = 10)

        master.grid_rowconfigure(6, weight=1)

        tes = button_ribbon(master=master, text="delete")
        tes.grid(row =7, column=0, sticky = "ew", padx = 20, pady=[0,10])

        return result

    def preference_widget(self, workspace: ctk.CTkFrame) -> ctk.CTkFrame:
        preference_frame = ctk.CTkFrame(workspace, width=200, corner_radius=0, fg_color=BACKGROUND_COLOR)
        preference_frame.grid(row=0, column=2, sticky="ns")

        preference_frame.grid_propagate(False)
        preference_frame.grid_columnconfigure(0, weight=1)

        # menambahkan label
        preference_label = ctk.CTkLabel(
            preference_frame, 
            text="Preference", 
            font=(FONT, 16, "bold"), 
            text_color=TEXT_COLOR,
            anchor="center" 
        )

        preference_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")  # 4. Label mengisi lebar kolom

        return preference_frame
    

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
    
    # def min fiture for content
    def code_panel(self, master) -> None:
        return None
        
    def sidebar_content(self, master) -> None:
        return None
    
if __name__ == "__main__":
    app = visual_programming()
    app.mainloop()
