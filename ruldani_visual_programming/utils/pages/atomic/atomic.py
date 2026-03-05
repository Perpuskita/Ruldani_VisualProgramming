import customtkinter as ctk
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils import color_manager as cm
import tkinter as tk

WIDTH = 160
HEIGHT_TEXT = 10
HEIGHT_ENTRY = 25

class button(ctk.CTkButton):
    def __init__(self, master, icon: str, size: int = 15, colour: str = cm.BACKGROUND_COLOR, hover_colour = cm.GREEN_PALLETE ):
        super().__init__(master=master, fg_color=colour, hover_color=hover_colour, height=size, width=size)
        ukuran: int = size - 3
        images = image(filename=icon, dimension=[ukuran,ukuran])
        self.configure(image=images, text="", width = ukuran, height=ukuran+15)

class button_sidebar(ctk.CTkButton):
    def __init__(self, master, button: str, subbutton: str, icon: str, size: int = 15, colour: str = cm.BACKGROUND_COLOR, hover_colour = cm.GREEN_PALLETE ):
        super().__init__(master=master, fg_color=colour, hover_color=hover_colour, height=15, width=15)
        
        self.identity = [button, subbutton]
        
        ukuran: int = size - 3
        images = image(filename=icon, dimension=[ukuran,ukuran])
        self.configure(image=images, text="", width = ukuran, height=ukuran+15)

    def binding_button(self) -> None:
        return None

class logo(ctk.CTkLabel):
    def __init__(self, master, logo_image: str, width = 40, height = 40):
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
        super().__init__(master, width=140, height=26, text="visual programming", fg_color=cm.ORANGE_PALLETE, text_color=cm.BACKGROUND_COLOR)
        self.toggle_on()

    def toggle_off(self):
        self.configure(text_color = cm.TEXT_COLOR, fg_color = cm.SECONDARY_COLOR,  hover_color=cm.BACKGROUND_COLOR)

    def toggle_on(self):
        self.configure(text_color = cm.BACKGROUND_COLOR, fg_color = cm.ORANGE_PALLETE,  hover_color=cm.SECONDARY_COLOR)

class button_code(ctk.CTkButton):
    def __init__(self, master ):
        super().__init__(master, width=120, height=26, text="code", fg_color=cm.BLUE_PALLETE, text_color= cm.BACKGROUND_COLOR, hover_color=cm.SECONDARY_COLOR)
        self.toggle_off()

    def toggle_off(self):
        self.configure(text_color = cm.TEXT_COLOR, fg_color = cm.SECONDARY_COLOR, hover_color = cm.BLUE_PALLETE)

    def toggle_on(self):
        self.configure(text_color = cm.TEXT_COLOR, fg_color = cm.BLUE_PALLETE)


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
        
class flowchart(ctk.CTkButton):
    def __init__(self, master, color: str):
        super().__init__(master=master, fg_color="transparent", width=40, height=10, text="namae")

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event):
        # Membuat jendela popup kecil (Toplevel)
        self.tip_window = tw = tk.Toplevel(self.widget)
        
        # Menghilangkan border jendela agar terlihat seperti tooltip
        tw.wm_overrideredirect(True)
        
        # Mengatur posisi tooltip (di sebelah kanan bawah kursor)
        x = self.widget.winfo_rootx() + 30
        y = self.widget.winfo_rooty() + 30
        tw.wm_geometry(f"+{x}+{y}")

        # Membuat label di dalam tooltip
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("arial", "10", "normal"))
        label.pack(ipadx=5, ipady=3)

    def hide_tip(self, event):
        # Menghancurkan jendela tooltip saat mouse keluar
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None