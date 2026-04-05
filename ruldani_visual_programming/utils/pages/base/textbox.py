import customtkinter as ctk
from ruldani_visual_programming.utils.models import highlight
import ruldani_visual_programming.utils.color_manager as cm

class textbox(ctk.CTkTextbox):
    def __init__(self, master):
        super().__init__(master=master)
        print("success")
        self.make_widget()

    def make_widget(self):
        self.configure(width=400, corner_radius=0, fg_color = cm.CODE_CONTENT)
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
