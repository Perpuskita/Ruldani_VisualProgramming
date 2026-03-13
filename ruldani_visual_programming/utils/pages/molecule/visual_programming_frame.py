import customtkinter as ctk
import random
import ruldani_visual_programming.utils.color_manager as cm
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils.pages.atomic import nodeberzier

class visual_programming_frame(ctk.CTkFrame):
    def __init__(self, master, text):
        super().__init__(master=master, width=100, height=30)
        self.master = master
        self.initial_position()
        self.make_inner_frame(text=text)
        self.make_input_node(types="imageInput1.png")
        self.make_output_node(types="imageOutput2.png")

    def initial_position(self) -> None:
        
        offset_x = random.randint(-20, 20) / self.master.winfo_width() 
        offset_y = random.randint(-20, 20) / self.master.winfo_height()

        # Place node in the center of the visual frame, with random offset
        relx = 0.5 + offset_x
        rely = 0.5 + offset_y

        self.place(relx=relx, rely=rely, anchor="center")
        return None
 
    def make_inner_frame(self, text: str) -> ctk.CTkLabel:
        new = ctk.CTkLabel(master=self, text=text, width=50, height=30, corner_radius=10, fg_color=cm.SECONDARY_COLOR)
        new.place(relx=0.5, rely=0.5, anchor="center")
        return new
    
    def make_input_node(self, types: str) -> ctk.CTkLabel:
        img = image(types,[10,10])
        new = ctk.CTkLabel(master=self, text="", image=img, height=10, width=10, fg_color="transparent")
        new.place(relx = 0.08, rely = 0.5, anchor = "center" )

        cointainer = []
        active_line = None

        hub:nodeberzier = nodeberzier(master=self.master, node_type="path", image_id=new, coor=self, nodeberzier_container=cointainer, active_line=active_line)
        return new
    
    def make_output_node(self, types: str) -> ctk.CTkLabel:
        img = image(types,[10,10])
        new = ctk.CTkLabel(master=self, text="", image=img, height=10, width=10, fg_color="transparent")
        new.place(relx = 0.92, rely = 0.5, anchor = "center" )
        return new