import customtkinter as ctk
import random
import ruldani_visual_programming.utils.color_manager as cm
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils.pages.base import nodeberzier, inner_frame

class visual_programming_frame(ctk.CTkFrame):
    def __init__(self, master, text, container: list, active_line):
        self.max_height = 26
        self.max_width  = 140

        super().__init__(master=master, width=self.max_width, height=self.max_height)
        self.master = master
        
        # make utils for visual programming frame
        self.input: list[nodeberzier] = []
        self.output: list[nodeberzier] = []
        self.input_label: list[ctk.CTkFrame] = []
        self.output_label: list[ctk.CTkFrame] = []
        
        # container for line
        self.tooltip = None
        self.container = container
        self.active_line = active_line
        
        # make all widget
        self.inner_frame:inner_frame = self.make_inner_frame(text=text)
        self.make_widget()
        
        # status selected
        self.selected = False

    def make_widget(self) -> None:

        # Place node in the center of the visual frame, with random offset
        relx = 0.5 
        rely = 0.5

        self.place(relx=relx, rely=rely, anchor="center")
        self.grid_propagate(False)

        # make dummy widget
        self.make_input_node(types="imageInput1.png")
        self.make_input_node(types="imageInput1.png")
        self.make_output_node(types="imageOutput2.png")

        # return None
        return None
 
    def make_inner_frame(self, text: str) -> inner_frame:
        new = inner_frame(master=self, text=text, max_width=self.max_width, max_height=self.max_height)

        # bind motion
        new.bind("<B1-Motion>", command=self.on_drag)
        new.grid_propagate(False)

        # bind tooltip
        # new.bind("<Enter>", self.tooltip_show)
        # new.bind("<Leave>", self.tooltip_hide)
        
        return new

    def make_input_node(self, types: str) -> nodeberzier:
        img = image(types,[10,10])
        
        # membuat rely sesuai panjang dari input labell
        lenght: int = len(self.input_label)
        rely: float = self.place_sycronitation(length=lenght)
        
        for i in range(lenght):
            self.input_label[i].place(relx = 0.08, rely = rely*(i+1), anchor = "center")
        
        # membuat label baru
        new = ctk.CTkLabel(master=self, text="", image=img, height=10, width=10, fg_color="transparent")
        new.place(relx = 0.08, rely = rely*(lenght+1), anchor = "center" )

        self.input_label.append(new)

        # membuat node berzier tipe baru
        hub:nodeberzier = nodeberzier(master=self.master, node_type="path", image_id=new, coor=self, nodeberzier_container=self.container, active_line=self.active_line)
        self.container.append(hub)
        self.input.append(hub)
        return hub
    
    def make_output_node(self, types: str) -> nodeberzier:
        img = image(types,[10,10])

        # membuat rely berdasarkan sisi dari input label
        lenght: int = len(self.output_label)
        rely: float = self.place_sycronitation(length=lenght)
        
        for i in range(lenght):
            self.output_label[i].place(relx = 0.92, rely = rely*(i+1), anchor = "center")
        
        # membuat label baru        
        new = ctk.CTkLabel(master=self, text="", image=img, height=10, width=10, fg_color="transparent")
        new.place(relx = 0.92, rely = rely*(lenght+1), anchor = "center" )

        self.output_label.append(new)

        hub:nodeberzier = nodeberzier(master=self.master, node_type="path", image_id=new, coor=self, nodeberzier_container=self.container, active_line=self.active_line)
        self.container.append(hub)
        self.output.append(hub)
        return hub
    
    def tooltip_show(self, e) -> None:
        print("show tooltip")
        return None
    
    def tooltip_hide(self, e) -> None:
        print("hide tooltip")
        return None

    def place_sycronitation(self, length: int) -> float:
        
        # new height get maximum
        new_height: int = self.max_height + (length*5)

        # new height condition
        if self.max_height < new_height:

            # configure self
            self.configure(height=new_height)
            
            # configure innerframe
            self.inner_frame.configure(height=new_height )

            self.max_height = new_height
        
        # return place
        return 1/(length+2)
    
    def on_drag(self, event) -> None:

        y = event.y_root - self.master.winfo_rooty() - self.master.winfo_height()/2
        x = event.x_root - self.master.winfo_rootx() - self.master.winfo_width()/2

        if y < int(-self.master.winfo_height()/2) + self.max_height/2 + 4:
            y = int(-self.master.winfo_height()/2 + self.max_height/2 + 4)
        
        elif y > int(self.master.winfo_height()/2) - self.max_height/2 - 4:
            y = int(self.master.winfo_height()/2 - self.max_height/2 - 4)

        if x < int( -self.master.winfo_width()/2 + self.max_width/2 ):
            x = int(-self.master.winfo_width()/2 + self.max_width/2 )

        elif x > int(self.master.winfo_width()/2) - self.max_width/2 :
            x = int(self.master.winfo_width()/2 - self.max_width/2 )
        
        self.update_node()
        self.place(x=x, y=y)
        return None
    
    # force update for node and line berzier
    def update_node(self) -> None:

        for input_node in self.input:
            input_node.force_update()

        for output_node in self.output:
            output_node.force_update()

    def toggle_selected(self):
        self.inner_frame.toggle_selected()
