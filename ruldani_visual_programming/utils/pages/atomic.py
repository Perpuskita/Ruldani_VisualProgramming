import customtkinter as ctk
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils import color_manager as cm

class button(ctk.CTkButton):
    def __init__(self, master, icon: str, size: int = 15, colour: str = cm.BACKGROUND_COLOR, hover_colour = cm.SECONDARY_COLOR ):
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

class preference():
    def __init__(self):
        pass

    def name(self, master: ctk.CTkFrame, placeholder: str ) -> ctk.CTkEntry:
        hasil: ctk.CTkEntry = ctk.CTkEntry(master=master, height=20, corner_radius=5, placeholder_text=placeholder, border_width=1, border_color="#ACACAC" )
        return hasil
    
    def name_error(self, master: ctk.CTkFrame, placeholder: str ) -> ctk.CTkEntry:
        hasil: ctk.CTkEntry = ctk.CTkEntry(master=master, width=140, height=20, corner_radius=5, placeholder_text=placeholder, border_color="#dd5b5b" )
        return hasil
    
class window(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200):
        super().__init__(master, width, height)

    