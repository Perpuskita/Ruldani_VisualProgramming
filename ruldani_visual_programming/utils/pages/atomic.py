import customtkinter as ctk
from ruldani_visual_programming.utils import image

image_ctk: image = image()

class button():
    def __init__(self, variant: str, color: str):
        pass
    
    def button_with_image(self, master: ctk.CTkFrame, size: list[int], icon_name: str = None, fg_color: str = "#EF9C66", hover_color: str = "#363636" ) -> ctk.CTkButton:
        button_frame: ctk.CTkButton = None
        height: int = size[0]
        width: int = size[1]

        # membuat button dengan icon image
        if icon_name != None :
            icon_image = image_ctk.get_image(icon_name, [width, height])
            button_frame = ctk.CTkButton(master=master, corner_radius= 5, image= icon_image, width=width, text="", height=height + 10, fg_color=fg_color, hover_color=hover_color)

        # membuat button tanpa image
        else :
            button_frame = ctk.CTkButton(master=master, width=width + 15, height=height + 10, text="", fg_color=fg_color, hover_color=hover_color)

        return button_frame 
    
    def button_selected_with_image(self, master: ctk.CTkFrame):
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