import customtkinter as ctk
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils import color_manager as cm

WIDTH = 160
HEIGHT_TEXT = 10
HEIGHT_ENTRY = 25

class button(ctk.CTkButton):
    def __init__(self, master, icon: str, size: int = 15, colour: str = cm.BACKGROUND_COLOR, hover_colour = cm.CYAN_PALLETE ):
        super().__init__(master=master, fg_color=colour, hover_color=hover_colour, height=size, width=size)
        ukuran: int = size - 3
        images = image(filename=icon, dimension=[ukuran,ukuran])
        self.configure(image=images, text="", width = ukuran, height=ukuran+15)

class logo(ctk.CTkLabel):
    def __init__(self, master, logo_image: str, width = 20, height = 20):
        logo_img: ctk.CTkImage = image(logo_image, [15,15]) 
        super().__init__(master, width, height, image = logo_img, text ="")

class button_ribbon(ctk.CTkButton):
    def __init__(self, master, text: str ):
        super().__init__(master, width=50, height=10, text=text, fg_color=cm.BACKGROUND_COLOR, hover_color=cm.SECONDARY_COLOR)

    def release_hover(self):
        self.configure(font=("concolas", 12))

    def on_hover(self):
        self.configure(font=("concolas", 12, "underline"))

class button_visual(ctk.CTkButton):
    def __init__(self, master ):
        super().__init__(master, width=120, height=26, text="visual programming", fg_color=cm.ORANGE_PALLETE, text_color=cm.BACKGROUND_COLOR, hover_color=cm.SECONDARY_COLOR)

class button_code(ctk.CTkButton):
    def __init__(self, master ):
        super().__init__(master, width=90, height=26, text="code", fg_color=cm.BLUE_PALLETE, text_color= cm.BACKGROUND_COLOR, hover_color=cm.SECONDARY_COLOR)

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

class window(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200):
        super().__init__(master, width, height)

class sidebar_class(ctk.CTkButton):
    def __init__(self, master, text: str ):
        dropdown: ctk.CTkImage = image("arrow_down.png", [16, 16])
        super().__init__(master, width=120, height=10, image=dropdown, text=text, fg_color=cm.BACKGROUND_COLOR, hover_color=cm.SECONDARY_COLOR, font=("Concolas", 12, "normal"), anchor="w" )
        