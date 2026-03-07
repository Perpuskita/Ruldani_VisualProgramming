from ruldani_visual_programming.utils.pages.atomic import button
import ruldani_visual_programming.utils.color_manager as cm
import customtkinter as ctk

class settings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master = master, width=40, fg_color = cm.BACKGROUND_COLOR, corner_radius=0)
        self.configure_panel()
        self.make_widget()

    def make_widget(self) -> None:
        img: list[str] = ["thumbnail_bar.png","cpm1.png", "cpm2.png", "cpm3.png"]

        for i, image in enumerate(img):
            atomic = button(master=self, icon=image)
            if i == 0 :
                atomic.grid(row=i, column=0, pady= (3, 5), padx=(5, 5), sticky="n")

            else :
                atomic.grid(row=i, column=0, pady= (5, 5), padx=(5, 5), sticky="n")

        self.grid_rowconfigure(len(img), weight=1) 

        tes = button(master=self, icon="settings.png")
        tes.grid(row=len(img) + 1, column=0, pady = 5, padx = 0, sticky="ns" )
        
        return None

    def configure_panel(self) -> None:
        self.grid(row=0, column=0, sticky="ns")
        self.grid_propagate(False)
        self.grid_columnconfigure(3, weight=1)
        return None