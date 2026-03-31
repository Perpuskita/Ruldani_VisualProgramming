import customtkinter as ctk
import random
import ruldani_visual_programming.utils.color_manager as cm
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils.pages.base import nodeberzier

class visual_programming_frame(ctk.CTkFrame):
    def __init__(self, master, text, container: list, active_line):
        super().__init__(master=master, width=100, height=30)
        self.master = master
        
        # make utils for visual programming frame
        self.tooltip = None
        self.container = container
        self.active_line = active_line
        
        # make all widget
        self.initial_position()
        self.make_inner_frame(text=text)
        self.input: nodeberzier = self.make_input_node(types="imageInput1.png")
        self.output: nodeberzier = self.make_output_node(types="imageOutput2.png")

        self.selected = False

    def initial_position(self) -> None:

        # Place node in the center of the visual frame, with random offset
        relx = 0.5 
        rely = 0.5

        self.place(relx=relx, rely=rely, anchor="center")
        return None
 
    def make_inner_frame(self, text: str) -> ctk.CTkLabel:
        new = ctk.CTkLabel(master=self, text=text, width=50, height=30, corner_radius=10, fg_color=cm.SECONDARY_COLOR)
        new.place(relx=0.5, rely=0.5, anchor="center")

        # bind motion
        new.bind("<Button-1>", command=self.on_click)
        new.bind("<B1-Motion>", command=self.on_drag)

        # bind tooltip
        new.bind("<Enter>", self.tooltip_show)
        new.bind("<Leave>", self.tooltip_hide)
        
        return new
    
    def tooltip_show(self, e) -> None:
        print("show tooltip")
        return None
    
    def tooltip_hide(self, e) -> None:
        print("hide tooltip")
        return None

    def make_input_node(self, types: str) -> nodeberzier:
        img = image(types,[10,10])
        new = ctk.CTkLabel(master=self, text="", image=img, height=10, width=10, fg_color="transparent")
        new.place(relx = 0.08, rely = 0.5, anchor = "center" )

        hub:nodeberzier = nodeberzier(master=self.master, node_type="path", image_id=new, coor=self, nodeberzier_container=self.container, active_line=self.active_line)
        self.container.append(hub)
        return hub
    
    def make_output_node(self, types: str) -> nodeberzier:
        img = image(types,[10,10])
        new = ctk.CTkLabel(master=self, text="", image=img, height=10, width=10, fg_color="transparent")
        new.place(relx = 0.92, rely = 0.5, anchor = "center" )

        hub:nodeberzier = nodeberzier(master=self.master, node_type="path", image_id=new, coor=self, nodeberzier_container=self.container, active_line=self.active_line)
        self.container.append(hub)
        return hub
    
    def on_drag(self, event) -> None:

        y = event.y_root - self.master.winfo_rooty() - self.master.winfo_height()/2
        x = event.x_root - self.master.winfo_rootx() - self.master.winfo_width()/2

        if y < int(-self.master.winfo_height()/2) + 15:
            y = int(-self.master.winfo_height()/2 + 15)

        if x < int( -self.master.winfo_width()/2 + 50):
            x = int(-self.master.winfo_width()/2 + 50)

        if y > int(self.master.winfo_height()/2) - 15:
            y = int(self.master.winfo_height()/2 - 15)

        if x > int(self.master.winfo_width()/2) - 50:
            x = int(self.master.winfo_width()/2 - 50)
        
        self.update_node()
        self.place(x=x, y=y)
        return None
    
    def update_node(self) -> None:
        self.input.force_update()
        self.output.force_update()

    def on_click(self, event) -> None:

        print("on click")
        return None