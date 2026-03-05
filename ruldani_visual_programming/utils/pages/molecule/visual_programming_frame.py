import customtkinter as ctk
import random
import ruldani_visual_programming.utils.color_manager as cm

class visual_programming_frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=90, height=30, fg_color="transparent")
        self.initial_position()

    def initial_position(self) -> None:
        
        offset_x = random.randint(-10, 10) / self.master.winfo_width() 
        offset_y = random.randint(-10, 10) / self.master.winfo_height()

        print(self.master.winfo_width())

        print(offset_y)

        # Place node in the center of the visual frame, with random offset
        relx = 0.5 
        rely = 0.5

        self.place(relx=relx, rely=rely, anchor="center")
        return None

 

