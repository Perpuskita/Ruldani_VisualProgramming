import os
from PIL import Image
import customtkinter as ctk
import tkinter as tk
import random
import pyperclip
from ruldani_visual_programming.utils import interpreter_code, nodeberzier, highlight, image
from ruldani_visual_programming.utils.pages import button, preference
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
        self.make_window([1080, 720])

    def make_window(self, geometry:list[int]) -> None:

        width = geometry[0]
        heigt = geometry[1]

        self.geometry(f"{width}x{heigt}")
        self.title("Ruldani - Visual Programming")
        
        # Configure columns and rows to allow resizing
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # configure workspace grid configure
        self.grid_columnconfigure(0, weight= 1)

        # make workspace and workspace widget
        workspace = self.workspace_panel()
        sidebar = self.sidebar_widget(workspace=workspace)
        content = self.content_widget(workspace=workspace)
        setting = self.setting_widget(workspace=workspace)
        preference = self.preference_widget(workspace=workspace)
        
        # make menubar and menubar widget
        menubar = self.menubar_panel()
        ribbon = self.ribbon_widget(menubar=menubar)

        setting_sidebar = self.setting_sidebar_widget(master=setting)
        preferences_menu = self.preference_menu(master=preference)
    
    def ribbon_widget(self, menubar: ctk.CTkFrame):
        btn_home = ctk.CTkButton(menubar, width=50, height=10, text="save", fg_color=BACKGROUND_COLOR, hover_color=SECONDARY_COLOR)
        btn_home.grid(row=0, column=1, padx=(10, 2), sticky="w")

        btn_home = ctk.CTkButton(menubar, width=50, height=10, text="load", fg_color=BACKGROUND_COLOR, hover_color=SECONDARY_COLOR)
        btn_home.grid(row=0, column=2, padx=2, sticky="w")

        btn_home = ctk.CTkButton(menubar, width=50, height=10, text="tools", fg_color=BACKGROUND_COLOR, hover_color=SECONDARY_COLOR)
        btn_home.grid(row=0, column=3, padx=2, sticky="w")

        btn_home = ctk.CTkButton(menubar, width=50, height=10, text="help", fg_color=BACKGROUND_COLOR, hover_color=SECONDARY_COLOR)
        btn_home.grid(row=0, column=4, padx=2, sticky="w")

        return btn_home

    def setting_sidebar_widget(self, master: ctk.CTkFrame):

        img: list[str] = ["cpm1.png", "cpm2.png", "cpm3.png"]

        for i, image in enumerate(img):
            atomic = button(master=master, image=image)
            if i == 0 :
                atomic.grid(row=i, column=0, pady= (12, 5), padx=(5, 5), sticky="n")

            else :
                atomic.grid(row=i, column=0, pady= (5, 5), padx=(5, 5), sticky="n")

        # setting = atomic.button_with_image(master=master, size=[15, 15], icon_name= "cpm2.png",fg_color= BACKGROUND_COLOR, hover_color=SECONDARY_COLOR)
        # setting.grid(row=1, column=0, pady= 5, padx=(5, 5), sticky="n")

        # setting = atomic.button_with_image(master=master, size=[15, 15], icon_name= "cpm3.png",fg_color= BACKGROUND_COLOR, hover_color=SECONDARY_COLOR)
        # setting.grid(row=2, column=0, pady= 5, padx=(5, 5), sticky="n")

        master.grid_rowconfigure(3, weight=1) 

        tes = button(master=master, image="settings.png")
        tes.grid(row=4, column=0, pady = 5, padx = 0, sticky="ns" )
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
        sidebar.grid(row=0, column=1, sticky="nsw")

        # 1. Kunci lebar sidebar agar tidak berubah sesuai isi
        sidebar.grid_propagate(False)
        sidebar.grid_columnconfigure(0, weight=1)

        # Create sidebar label
        sidebar_label = ctk.CTkLabel(
            sidebar, 
            text="Connection", 
            font=(FONT, 16, "bold"), 
            text_color=TEXT_COLOR,
            anchor="center"  # 3. Teks rata tengah di dalam label
        )
        sidebar_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")  # 4. Label mengisi lebar kolom

        return sidebar

    def preference_menu(self, master) -> ctk.CTkEntry:
        preferences = preference()
        result: ctk.CTkEntry = preferences.name(master=master, placeholder="tes")
        result.grid(row=1, column=0, padx=[20,10], pady=10, sticky ="ew")

        return result

    def preference_widget(self, workspace: ctk.CTkFrame) -> ctk.CTkFrame:
        preference_frame = ctk.CTkFrame(workspace, width=200, corner_radius=0, fg_color=BACKGROUND_COLOR)
        preference_frame.grid(row=0, column=3, sticky="ns")

        preference_frame.grid_propagate(False)
        preference_frame.grid_columnconfigure(0, weight=1)

        # menambahkan label
        preference_label = ctk.CTkLabel(
            preference_frame, 
            text="Preference", 
            font=(FONT, 16, "bold"), 
            text_color=TEXT_COLOR,
            anchor="center"  # 3. Teks rata tengah di dalam label
        )

        preference_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")  # 4. Label mengisi lebar kolom

        return preference_frame
    
    def content_widget(self, workspace: ctk.CTkFrame):
        # Create content area and other widgets
        content = ctk.CTkFrame(workspace, corner_radius=0, fg_color="#252525")
        content.grid(row=0, column=2, sticky="nsew")
        
        return content

    # make workspace panel
    def workspace_panel(self):
        workspace = ctk.CTkFrame(self, corner_radius=0)
        workspace.grid(row=1, column=0, sticky="nsew")
        workspace.grid_columnconfigure(0, weight=0)
        workspace.grid_columnconfigure(1, weight=0)
        workspace.grid_columnconfigure(2, weight=1)
        workspace.grid_columnconfigure(3, weight=0)
        workspace.grid_rowconfigure(0, weight=1)

        
        return workspace

    # make menubar panel
    def menubar_panel(self):
        menubar = ctk.CTkFrame(self, width=1080, height=30)
        menubar.configure(fg_color= BACKGROUND_COLOR, corner_radius=0)
        menubar.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        menubar.grid_propagate(False)
        menubar.grid_columnconfigure((0, 1, 2), weight=0) 
        
        logo_str: ctk.CTkImage = image(LOGO_IMAGE, [15,15])
        logo: ctk.CTkLabel = ctk.CTkLabel( master=menubar, image=logo_str, text= "")
        logo.grid(row=0, column=0, padx=(10,10), pady=2, sticky="nsew")

        return menubar
        
if __name__ == "__main__":
    app = visual_programming()
    app.mainloop()
