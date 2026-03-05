import customtkinter as ctk
from ruldani_visual_programming.utils.pages.atomic import button_ribbon, button
import ruldani_visual_programming.utils.color_manager as cm

class ribbon(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=1080, height=30, fg_color=cm.BACKGROUND_COLOR )
        self.initial_state()
        self.panel_configure()

    def initial_state(self) -> None:
        text_title: list = ["save", "load", "tools", "view"]

        for i, title in enumerate(text_title):
            padx: int = 5
            if i == 0 :
                padx = 4
                
            btn_home = button_ribbon(master=self, text=title)
            btn_home.grid(row=0, column=i, pady=5, padx=(padx, 2), sticky="w")

        self.grid_columnconfigure(len(text_title), weight=1) 

        tes = button(master=self, icon="help.png")
        tes.grid(column=len(text_title) + 1, row=0, pady = 0, padx = 0, sticky="ns" )
    
    def panel_configure(self) -> None:
        self.grid(row=0, column=1, sticky="ew", padx=0, pady=0)
        self.grid_propagate(False)