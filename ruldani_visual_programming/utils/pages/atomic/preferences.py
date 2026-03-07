import customtkinter as ctk
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils import color_manager as cm

WIDTH = 160
HEIGHT_TEXT = 10
HEIGHT_ENTRY = 25

class preference(ctk.CTkEntry):
    def __init__(self, master, text: str= "none" ):
        super().__init__(master=master, width=WIDTH, height=HEIGHT_ENTRY, corner_radius=5, placeholder_text="defaut name", border_color=cm.SECONDARY_COLOR)
    
class preference_text(ctk.CTkLabel):
    def __init__(self, master, text:str):
        super().__init__(master, width = 50, height = HEIGHT_TEXT, text=text, anchor="w", fg_color=cm.BACKGROUND_COLOR)

class preference_error(ctk.CTkLabel):
    def __init__(self, master, text:str):
        super().__init__(master, width = 50, height = HEIGHT_TEXT, text=text, anchor="e", fg_color=cm.BACKGROUND_COLOR, text_color=cm.RED_PALLETE)

class preference_dropdown(ctk.CTkOptionMenu):
    def __init__(self, master, values: list[str]):
        super().__init__(master, width=WIDTH, height=HEIGHT_ENTRY, values=values, text_color=cm.TEXT_COLOR)
        self.set(value=values[0])
        self.configure(dropdown_text_color = cm.TEXT_COLOR, button_color =cm.SECONDARY_COLOR, fg_color = cm.SECONDARY_COLOR, button_hover_color = cm.BLUE_PALLETE)
