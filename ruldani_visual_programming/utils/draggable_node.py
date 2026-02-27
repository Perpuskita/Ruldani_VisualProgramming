import ruldani_visual_programming.utils.color_manager as cm
import customtkinter as ctk
from ruldani_visual_programming.utils import interpreter_code, nodeberzier
import os

from PIL import Image

# Define colors
CYAN_PALLETE = cm.CYAN_PALLETE
ORANGE_PALLETE = cm.ORANGE_PALLETE
YELLOW_PALLETE = cm.ORANGE_PALLETE
LIGHT_GREEN_PALLETE = cm.LIGHT_GREEN_PALLETE

# non pallete colors
SECONDARY_COLOR = cm.SECONDARY_COLOR
BACKGROUND_COLOR = cm.BACKGROUND_COLOR
TEXT_COLOR = cm.TEXT_COLOR
DARK_COLOR = cm.DARK_COLOR

# Define Font
FONT = "Consolas"

node_container = []
nodeberzier_container = []
active_line = None

base_dir = base_dir = os.path.dirname(os.path.abspath(__file__))

def get_icon_path(filename):
    return os.path.join(base_dir, "icons", filename)

# Kelas untuk Dragable Node
class DraggableNode(ctk.CTkFrame):

    def __init__(self, master, name, icon, visual_framer, preference_frame: ctk.CTkFrame, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Adaptation subbutton properties
        self.name = name.sub_button_name
        self.configure(width=65, 
                       height=50, 
                       fg_color="transparent", 
                       corner_radius=5)
        self.preferences = interpreter_code(self.name).get_interpreter()
        self.preferences_frame = preference_frame

        # Create icon label
        self.on_drag = False
        self.icon_bg = ctk.CTkLabel(self, 
                                    width=50, 
                                    height=50, 
                                    corner_radius=5, 
                                    fg_color=SECONDARY_COLOR, 
                                    text="")
        self.icon_bg.place(relx=0.5, 
                           rely=0.5, 
                           anchor="center")
        self.icon_label = ctk.CTkLabel(self, 
                                       fg_color=SECONDARY_COLOR, 
                                       image=icon, 
                                       text="")
        self.icon_label.place(relx=0.5, rely=0.5, anchor="center")

        # Add a small delete button (e.g., "X") on the top-right corner of the node
        self.delete_button = ctk.CTkButton(
            self,
            text="x",
            width=5,
            height=5,
            fg_color="#FF1111",  # Red color for delete button
            hover_color="#FF6666",
            command=self.delete_node,
            text_color="white",
            font=(FONT, 10, "bold")
        )
        self.delete_button.place(x = 5, 
                                 rely=0.1, 
                                 anchor="center")  # Position at top-right corner
        self.delete_button.lower()
        self.delete_button_hover = False
        self.node_container = []
        self.output = None

        if self.name == "folder" or self.name == "gdrive folder":
            self.append(self.node_icon_output(visual_framer))

        else :
            #berziercurve
            self.append(self.node_icon_output(visual_framer))
            self.append(self.node_icon_input(visual_framer))

        self.pos_x_init = 0
        self.pos_y_init = 0
        self._enable_dragging()

        # binding for base 
        # hover & hover leave
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_hover_leave)

        # binding icon bg
        # hover & hover leave
        self.icon_bg.bind("<Enter>", self.on_hover)
        self.icon_bg.bind("<Leave>", self.on_hover_leave)
        
        # binding icon label 
        # hover & hover leave
        self.icon_label.bind("<Enter>", self.on_hover)
        self.icon_label.bind("<Leave>", self.on_hover_leave)

        # binding button delete
        # hover & hover leave
        self.delete_button.bind("<Enter>", self.on_delete_button_hover)
        self.delete_button.bind("<Leave>", self.on_delete_button_leave)

        # indicator for hover delete
        self.on_hover_delete = False

    def append(self, Neo):
        nodeberzier_container.append(Neo)
        self.node_container.append(Neo)
    
    
    # Preferences Menu panel settings
    def update_preference(event, self):
        
        for widget in self.preference_frame.winfo_children():
            widget.destroy()
        
        title = ctk.CTkLabel(master=self.preference_frame, text="Preferences", font=(FONT, 16, "bold"))
        title.pack(pady=20, padx = 60)

        def update_info(event=None):
            self.preferences.update_data(*(val.get() for val in values))

        values = []

        for node in self.preferences.atribute():  
            if node[0] == "nama" :
                name_label = ctk.CTkLabel(master=self.preference_frame, text="Name", font=(FONT, 14))
                name_label.pack(pady=(0,0))
                name_entry = ctk.CTkEntry(master=self.preference_frame)
                name_entry.insert(0, node[1])
                name_entry.pack(pady=(0,10))
                name_entry.bind("<KeyRelease>", update_info)
                values.append(name_entry)

            elif node[0] == "framework":
                framework_label = ctk.CTkLabel(master=self.preference_frame, text="Framework", font=(FONT, 14))
                framework_label.pack(pady=(10,0))
                framework_combo = ctk.CTkComboBox(master=self.preference_frame, values=node[1], command= update_info)
                framework_combo.pack(padx=30,pady=0)
                framework_combo.set(node[2])
                values.append(framework_combo)

            elif node[0] == "link":
                link_label = ctk.CTkLabel(master=self.preference_frame, text="Link", font=(FONT, 14))
                link_label.pack(pady=(20, 0))
                link_entry = ctk.CTkEntry(master=self.preference_frame)
                link_entry.insert(0, node[1])  # Menampilkan link awal
                link_entry.pack(pady=0)
                # Event binding untuk memperbarui data setiap kali teks diubah
                link_entry.bind("<KeyRelease>", update_info)
                values.append(link_entry)

    # node icon input
    def node_icon_input(self, visual_framer):
        type_node = "path"
        node_icon_output_image= ctk.CTkLabel(self,
                                             height=5,
                                             width=5,
                                             fg_color="transparent",
                                             image=self._node(get_icon_path("imageInput1.png")),
                                             text="")
        node_icon_output_image.place(x=5,
                                     rely=0.5,
                                     anchor="center")
            
        return nodeberzier(visual_framer,type_node,node_icon_output_image, self, nodeberzier_container, active_line)
    # node icon output
    def node_icon_output(self, visual_framer):
        type_node = "path"
        node_icon_output_image= ctk.CTkLabel(self,
                                             height=5,
                                             width=5,
                                             fg_color="transparent",
                                             image=self._node(get_icon_path("imageOutput1.png")),
                                             text="")
        node_icon_output_image.place(x=60,
                                     rely=0.5,
                                     anchor="center")
        
        self.output = nodeberzier(visual_framer,type_node,node_icon_output_image, self, nodeberzier_container, active_line )
        return self.output
    
    def node_generator(self):

        self.node_icon = ctk.CTkLabel(self, 
                                      height=5, 
                                      width=5, 
                                      fg_color="transparent", 
                                      image=self._node(get_icon_path("imageInput1.png")), 
                                      text="")
        self.node_icon.place(x=60, rely=0.5, anchor="center")
        #pywin.set_opacity(self.node_icon, value = 0.5)

        self.node_icon = ctk.CTkLabel(self, height=5, width=5, fg_color="transparent", image=self._node(get_icon_path("imageOutput1.png")), text="")
        self.node_icon.place(x=5, rely=0.5, anchor="center")

    def void_preference(self): 
        for widget in self.preference_frame.winfo_children():
            widget.destroy()
        
        title = ctk.CTkLabel(master=self.preference_frame, text="Preferences", font=(FONT, 16, "bold"))
        title.pack(pady=20, padx = 60)
        

    def delete_node(self):
        """Delete the current node from the visual frame and node_container."""
        # Remove the node from node_container

        for Node in self.node_container:
            Node.delete_line()

        if self in node_container:
            node_container.remove(self)

        # Update the sidebar buttons when a node is deleted
        update_sidebar_buttons()
        self.void_preference()
        
        # Destroy the node widget from the UI
        self.destroy()

    def on_hover(self, event=None):
        """Show the delete button when the node is hovered."""
        if len(node_container) > 1:
            if self != node_container[0] :
                self.delete_button.lift()  # Bring the delete button to the front
        else:
            self.delete_button.lift() 

    def on_hover_leave(self, event=None):
        """Hide the delete button when the hover ends."""
        self.delete_button.lower()  # Send the delete button to the back

    def on_delete_button_hover(self, event=None):
        """Set delete button hover flag to True when hovered."""
        self.delete_button_hover = True
        self.delete_button.lift()  # Keep the delete button visible

    def on_delete_button_leave(self, event=None):
        """Reset delete button hover flag when no longer hovered."""
        self.delete_button_hover = False
        self.delete_button.lower()  # Hide the delete button

    def _node(self, icon):
        icon_path = get_icon_path(icon)
        return ctk.CTkImage(Image.open(icon_path), size=(10, 10))

    def _enable_dragging(self):

        """Enable dragging functionality for the widget."""

        def on_drag_start(event):
            # Store initial mouse position and widget's position
            self.start_x = event.x_root
            self.start_y = event.y_root
            

        def on_drag_motion(event):
            # Calculate the new position based on the movement
            self.new_x = event.x_root - self.start_x + self.pos_x_init
            self.new_y = event.y_root - self.start_y + self.pos_y_init
            # Move the widget to the new position
            self.place(x=self.new_x, y=self.new_y)
            
            for Node in self.node_container:
                Node.force_update()

        def release_motion(event):
            # Update initial position after dragging
            self.pos_x_init = self.new_x
            self.pos_y_init = self.new_y

        # Bind mouse events to the widget
        self.icon_bg.bind("<Button-1>", on_drag_start)
        self.icon_bg.bind("<B1-Motion>", on_drag_motion)
        self.icon_bg.bind("<ButtonRelease-1>", release_motion)
        self.icon_bg.bind("<Button-3>", lambda event: self.update_preference(event, self))

        # Also bind the same events to the icon label
        self.icon_label.bind("<Button-1>", on_drag_start)
        self.icon_label.bind("<B1-Motion>", on_drag_motion)
        self.icon_label.bind("<ButtonRelease-1>", release_motion)
        self.icon_label.bind("<Button-3>", lambda event: self.update_preference(event, self))
    
    def code(self, input):
        return self.preferences.code_saver(input)


