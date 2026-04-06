import customtkinter as ctk
from ruldani_visual_programming.utils.models import highlight
import ruldani_visual_programming.utils.color_manager as cm

class textbox(ctk.CTkTextbox):
    def __init__(self, master):
        super().__init__(master=master)
        self.zoom:int = 14
        self.make_widget()

    def make_widget(self):
        self.configure(width=400, font=("Helvetica", self.zoom),  corner_radius=0, fg_color = cm.CODE_CONTENT, padx=20, pady=20)
        self.configure(state="disabled")
        return None
    
    def remove_text(self):
        self.configure(state="normal")
        self.delete(0.0, "end")
        self.configure(state="disabled")
        return None
    
    def set_text(self, text: str) -> None:
        # reset textbox
        self.remove_text()

        # make highlight sintaks
        self.configure(state="normal")
        highlight(textbox=self, text=text)
        self.configure(state="disabled")
        
        return None

    def zoom_in(self):
        print("zoom in")
        if self.zoom >= 20 :
            return None

        
        self.zoom += 2
        self.configure(font=("Helvetica", self.zoom))
        return None
    
    def zoom_out(self) -> None:
        print("zoom in")

        if self.zoom <= 10:
            return None

        self.zoom -= 2
        self.configure(font=("Helvetica", self.zoom))
        return None