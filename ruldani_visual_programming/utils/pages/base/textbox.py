import customtkinter as ctk
from ruldani_visual_programming.utils.models import highlight

class textbox(ctk.CTkTextbox):
    def __init__(self, master):
        super().__init__(master=master)
        self.make_widget()

    def make_widget(self):
        self.configure(width=400, corner_radius=0, state="disabled")
        self.insert("0.0", "Some example text!\n" * 50)
        return None
    
    def remove_text(self):
        self.delete(0.0, "end")
        return None
    
    def set_text(self, text: str) -> None:
        # reset textbox
        self.remove_text()

        # make highlight sintaks
        highlight_sytax: highlight = highlight(textbox=self, text=text)
        return None
