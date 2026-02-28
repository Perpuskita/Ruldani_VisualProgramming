import customtkinter as ctk
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils import color_manager as cm

class button(ctk.CTkButton):
    def __init__(self, master, title: str = None, image: str = None, size: list[str] = [15,15], colour: str = cm.BACKGROUND_COLOR, hover_colour = cm.SECONDARY_COLOR ):
        super().__init__(master=master, fg_color=colour, hover_color=hover_colour, height=size[0], width=size[1])

        if title != None and image != None:
            self.with_text(title)
        
        elif title is not None :
            self.with_text(title)
        
        else :
            self.with_image(image_name=image)

    def with_text(self, title: str) -> None:
        self.configure(text=title, width=50, height=50)
        return None
    
    def with_image(self, image_name: str ) -> None:
        ukuran: int = 12
        images = image(filename=image_name, dimension=[ukuran,ukuran])
        self.configure(image=images, text="", width = ukuran, height=ukuran+15)
        return None
    
    def set_active(self) -> None:
        return None

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

    