import customtkinter as ctk
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils import color_manager as cm
import tkinter as tk

WIDTH = 160
HEIGHT_TEXT = 10
HEIGHT_ENTRY = 25

class button(ctk.CTkButton):
    def __init__(self, master, icon: str, size: int = 15, colour: str = cm.BACKGROUND_COLOR, hover_colour = cm.GREEN_PALLETE ):
        super().__init__(master=master, fg_color=colour, hover_color=hover_colour)
        ukuran: int = size - 3
        images = image(filename=icon, dimension=[ukuran,ukuran])
        self.configure(image=images, text="", width = ukuran, height=ukuran+15)

    def on_active(self):
        return None

class button_sidebar(ctk.CTkButton):
    def __init__(self, master, button: str, subbutton: str, icon: str, size: int = 15, colour: str = cm.BACKGROUND_COLOR, hover_colour = cm.GREEN_PALLETE ):
        super().__init__(master=master, fg_color=colour, hover_color=hover_colour, height=15, width=15)
        
        self.identity = [button, subbutton]
        
        ukuran: int = size - 3
        images: image = image(filename=icon, dimension=[ukuran,ukuran])
        self.configure(image=images, text="", width = ukuran, height=ukuran+15)

    def binding_button(self) -> None:
        return None

class button_ribbon(ctk.CTkButton):
    def __init__(self, master, text: str ):
        super().__init__(master, width=50, height=10, text=text, fg_color=cm.BACKGROUND_COLOR, hover_color=cm.SECONDARY_COLOR)

    def release_hover(self):
        self.configure(font=("concolas", 12))

    def on_hover(self):
        self.configure(font=("concolas", 12, "underline"))