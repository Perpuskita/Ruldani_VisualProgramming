import customtkinter as ctk
from ruldani_visual_programming.utils.color_manager import SECONDARY_COLOR, GREEN_PALLETE

class inner_frame(ctk.CTkLabel):
    
    def __init__(self, master, text: str, max_width: int, max_height: int):
        
        self.color_selected = GREEN_PALLETE
        self.color_unselect = SECONDARY_COLOR

        super().__init__(master=master, text=text, width=int(max_width*86/100), height=max_height, corner_radius=10, fg_color=self.color_unselect)
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.selected = False

    def toggle_selected(self):
        self.selected = not self.selected

        if self.selected :
            self.configure( fg_color = self.color_selected )
        else :
            self.configure( fg_color = self.color_unselect )