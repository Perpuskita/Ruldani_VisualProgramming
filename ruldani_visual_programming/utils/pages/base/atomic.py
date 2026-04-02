import customtkinter as ctk
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils import color_manager as cm
import tkinter as tk

WIDTH = 160
HEIGHT_TEXT = 10
HEIGHT_ENTRY = 25

class logo(ctk.CTkLabel):
    def __init__(self, master, logo_image: str, width = 40, height = 40):
        logo_img: ctk.CTkImage = image(logo_image, [15,15]) 
        super().__init__(master, width, height, text ="")
        self.configure(image=logo_img)

class button_visual(ctk.CTkButton):
    def __init__(self, master ):
        super().__init__(master, width=140, height=26, text="visual programming", fg_color=cm.ORANGE_PALLETE, text_color=cm.BACKGROUND_COLOR)

    def toggle_off(self):
        self.configure(text_color = cm.TEXT_COLOR, fg_color = cm.SECONDARY_COLOR,  hover_color=cm.ORANGE_PALLETE)

    def toggle_on(self):
        self.configure(text_color = cm.BACKGROUND_COLOR, fg_color = cm.ORANGE_PALLETE,  hover_color=cm.ORANGE_PALLETE)


class button_code(ctk.CTkButton):
    def __init__(self, master ):
        super().__init__(master, width=120, height=26, text="code", fg_color=cm.BLUE_PALLETE, text_color= cm.BACKGROUND_COLOR, hover_color=cm.SECONDARY_COLOR)

    def toggle_off(self):
        self.configure(text_color = cm.TEXT_COLOR, fg_color = cm.SECONDARY_COLOR, hover_color = cm.BLUE_PALLETE)

    def toggle_on(self):
        self.configure(text_color = cm.BACKGROUND_COLOR, fg_color = cm.BLUE_PALLETE)

class window(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200):
        super().__init__(master, width, height)

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