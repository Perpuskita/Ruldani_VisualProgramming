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
    def __init__(self, master):
        super().__init__(master, width = 50, height = HEIGHT_TEXT, text="", anchor="e", fg_color=cm.BACKGROUND_COLOR, text_color=cm.RED_PALLETE)

class preference_dropdown(ctk.CTkOptionMenu):
    def __init__(self, master, values: list[str]):
        super().__init__(master, width=WIDTH, height=HEIGHT_ENTRY, values=values, text_color=cm.TEXT_COLOR)
        self.set(value=values[0])
        self.configure(dropdown_text_color = cm.TEXT_COLOR, button_color =cm.SECONDARY_COLOR, fg_color = cm.SECONDARY_COLOR, button_hover_color = cm.BLUE_PALLETE)

class preferences_connection_name(ctk.CTkLabel):
    def __init__(self, master, nama_node: str, connection_name: str):
        super().__init__(master=master, height=5, width=140, fg_color=cm.GREEN_PALLETE, anchor="w")

    def make_widget(self) -> None:
        return None

class preferences_connection_status(ctk.CTkLabel):
    def __init__(self, master):
        super().__init__(master, height= 5, width=140, fg_color=cm.GREEN_PALLETE, anchor="w")
        self.connection_release()

    def connection_release(self) -> None:
        self.configure(text="halo", fg_color=cm.RED_PALLETE)
        return None
    
    def connection_set(self) -> None:
        return None
    
class preferences_hidden_button(ctk.CTkButton):
    def __init__(self, master):
        super().__init__(master, width = 20, height = 80, text="", fg_color=cm.VISUAL_CONTENT, hover_color=cm.VISUAL_CONTENT, corner_radius=0)
        self.on_release_asset: image = image(filename="toggle_preferences.png", dimension=[12,48])
        self.on_hide_asset: image = image(filename="toggle_preferences2.png", dimension=[12,48])
        self.hide = False
        self.configure(image=self.on_hide_asset, text="", width = 10, height=50)

    def make_widget(self)-> None:
        self.on_release()
    
    def on_hover(self) -> None:
        # image ganti on hover preferences
        return None
    
    def on_release(self) -> None:
        # image ganti on release preferences
        self.configure(image=self.on_release_asset)
        return None
    
    def toggle(self)-> None:
        # hide toggle
        if self.hide:
            self.configure(image=self.on_hide_asset)
        
        # show toggle
        else:
            self.configure(image=self.on_release_asset)

        self.hide = not self.hide
        return None
