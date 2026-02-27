import os
from PIL import Image
import customtkinter as ctk
import random
import pyperclip
from ruldani_visual_programming.utils import interpreter_code, nodeberzier, highlight
import tkinter as tk
import ruldani_visual_programming.utils.color_manager as cm

from ruldani_visual_programming.utils import Button, SubButton

# Atur mode tampilan (light/dark)
ctk.set_appearance_mode("dark")

# Define your base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

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

# Define constant toggle visual or code
toggle_visual_or_code = True
node_container = []
nodeberzier_container = []
zoom_level = 1.0
active_line = None

# Kelas untuk Dragable Node
class DraggableNode(ctk.CTkFrame):

    def __init__(self, master, name, icon, visual_framer, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Adaptation subbutton properties
        self.name = name.sub_button_name
        self.configure(width=65, 
                       height=50, 
                       fg_color="transparent", 
                       corner_radius=5)
        self.preferences = interpreter_code(self.name).get_interpreter()

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

    def delete_node(self):
        """Delete the current node from the visual frame and node_container."""
        # Remove the node from node_container

        for Node in self.node_container:
            Node.delete_line()

        if self in node_container:
            node_container.remove(self)

        # Destroy the node widget from the UI
        self.destroy()
        # Update the sidebar buttons when a node is deleted
        update_sidebar_buttons()
        void_preference()

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
        self.icon_bg.bind("<Button-3>", lambda event: update_preference(event, self))

        # Also bind the same events to the icon label
        self.icon_label.bind("<Button-1>", on_drag_start)
        self.icon_label.bind("<B1-Motion>", on_drag_motion)
        self.icon_label.bind("<ButtonRelease-1>", release_motion)
        self.icon_label.bind("<Button-3>", lambda event: update_preference(event, self))
    
    def code(self, input):
        return self.preferences.code_saver(input)

if __name__ == "__main__":
    
    def get_icon_path(filename):
        return os.path.join(base_dir, "icons", filename)

    # Define buttons and sub-buttons
    buttons = [
        Button("Input System", "home.png", [
            # sub button folder
            SubButton("folder",
                      "folder.png",
                      LIGHT_GREEN_PALLETE),
            # sub button gdrive
            SubButton("gdrive folder",
                      "gdrive.png",
                      LIGHT_GREEN_PALLETE)
        ]),
        Button("Konsep Pendahuluan", "cpm1.png", [
            # sub button pembentukan citra
            SubButton("pembentukan citra",
                      "pembentukan citra.png",
                      CYAN_PALLETE),
        ]),
        Button("Pengolahan\nCitra digital", "cpm2.png", [
            # sub button analisa binner
            SubButton("analisa biner",
                      "analisa_citra_biner.png",
                      YELLOW_PALLETE),
            # sub button analisa abu
            SubButton("analisa abu",
                      "analisa_citra_abu.png",
                      YELLOW_PALLETE),
            # sub button transformasi fourier
            SubButton("transformasi fourier",
                      "transformasi_fourier.png",
                      YELLOW_PALLETE)
        ]),
        Button("Klasifikasi dan        \n Pengenalan Object", "cpm3.png", [
            # sub button deteksi tepi
            SubButton("deteksi tepi",
                      "deteksi_tepi.png",
                      ORANGE_PALLETE),
            # sub button ekstasi fitur
            SubButton("ekstraksi_fitur",
                      "ekstraksi_fitur.png",
                      ORANGE_PALLETE)
        ])
    ]

    def workspace_panel(workspace: ctk.CTkFrame):
        workspace.grid(row=1, column=0, sticky="nsew")
        workspace.grid_columnconfigure(0, weight=0)
        workspace.grid_columnconfigure(1, weight=0)
        workspace.grid_columnconfigure(2, weight=1)
        workspace.grid_columnconfigure(3, weight=0)
        workspace.grid_rowconfigure(0, weight=1)

    def menubar_panel(menu_bar: ctk.CTkFrame):
        menu_bar.configure(fg_color= BACKGROUND_COLOR, corner_radius=0)
        menu_bar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)


    text_code = ""

    paneling = { "sidebar": 1 } 

    # Create main window
    root = tk.Tk()
    root.geometry("1080x720")
    root.title("Ruldani - Visual Programming")
    
    # Configure columns and rows to allow resizing
    root.grid_rowconfigure(0, weight=0)
    root.grid_rowconfigure(1, weight=1)

    # configure workspace grid configure
    root.grid_columnconfigure(0, weight= 1)

    menu_bar = ctk.CTkFrame(root, width=1080, height=30)
    menubar_panel(menu_bar=menu_bar)

    workspace = ctk.CTkFrame(root, corner_radius=0)
    workspace_panel(workspace=workspace)

    # Create sidebar frame
    setting = ctk.CTkFrame(workspace, width=50, corner_radius=0, fg_color=BACKGROUND_COLOR)
    setting.grid(row=0, column=0, sticky="ns")

    # Create sidebar frame
    sidebar = ctk.CTkFrame(workspace, width=100, corner_radius=0, fg_color=BACKGROUND_COLOR)
    sidebar.grid(row=0, column=1, sticky="nsw")
    
    # Create content area and other widgets
    content = ctk.CTkFrame(workspace, width=800, corner_radius=0, fg_color="#252525")
    content.grid(row=0, column=2, sticky="nsew")  # Make content frame expandable

    preference_frame = ctk.CTkFrame(workspace, width=200, corner_radius=0, fg_color=BACKGROUND_COLOR)
    preference_frame.grid(row=0, column=3, sticky="ns")

    # Create sidebar label
    sidebar_label = ctk.CTkLabel(sidebar, text="Connection", font=(FONT, 16, "bold"), text_color=TEXT_COLOR)
    sidebar_label.grid(row=0, column=0, padx=20, pady=20)

    # Function to create main sidebar buttons
    def create_sidebar_buttons():
        for i, button in enumerate(buttons):
            # Create main button with icon and text
            main_button = ctk.CTkButton(
                master=sidebar,
                text=f" {button.button_name}",
                image=button.icon_button,
                compound="left",
                command=lambda b=button: toggle_expand(b),
                height=25,
                width=180,
                anchor="w",
                corner_radius=5,
                fg_color="transparent",
                hover_color=SECONDARY_COLOR
            )
            main_button.grid(row=i*2+1, column=0, padx=5, pady=5, sticky="w")
            button.main_button = main_button

            # Create frame for sub buttons
            subbutton_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
            subbutton_frame.grid(row=i*2+2, column=0, padx=30, pady=0, sticky="w")
            subbutton_frame.grid_remove()  # Initially hide the frame
            
            button.subbutton_frame = subbutton_frame  # Assign the frame to the button
            
            # Create sub buttons inside frame
            max_columns = 3
            for j, sub_button in enumerate(button.sub_buttons):
                subbutton = ctk.CTkButton(
                    master=subbutton_frame,
                    text="",
                    image=sub_button.sub_button_icon,
                    height=20,
                    width=20,
                    corner_radius=5,
                    fg_color="transparent",
                    hover_color=sub_button.hover_color
                )
                subbutton.grid(row=j // max_columns, column=j % max_columns, padx=5, pady=5)

                # Bind hover events
                subbutton.bind("<Enter>", 
                               lambda event,
                               icon=sub_button._create_image(60,60),
                               name=sub_button.sub_button_name: 
                               show_frame(event, icon, name))
                subbutton.bind("<Leave>", hide_frame)
                subbutton.bind("<Double-1>", 
                               lambda event,icon=sub_button._create_image(30,30),
                               button_name=sub_button:
                               on_double_click(event, button_name,icon))
                

        update_sidebar_buttons()

    def toggle_expand_off(button: ctk.CTkButton):
        button.toggle_expand_off()
        if button.expand_status:
            button.subbutton_frame.grid()
            button.main_button.configure(fg_color=SECONDARY_COLOR)

        else:
            button.subbutton_frame.grid_remove()
            button.main_button.configure(fg_color="transparent", hover_color=SECONDARY_COLOR)
   
    def  update_sidebar_buttons(): 

        if not node_container:
            for index in range(1, len(buttons)):
                buttons[index].main_button.configure(state="disabled")
                toggle_expand_off(buttons[index])
            buttons[0].main_button.configure(state="normal")
        
        else :
            for index in range(1, len(buttons)):
                buttons[index].main_button.configure(state="normal")
            buttons[0].main_button.configure(state="disabled")
            toggle_expand_off(buttons[0])

    def on_double_click(event, name, icon):
        global toggle_visual_or_code
        if toggle_visual_or_code:  # If the visual frame is active
            spawn_node(name, icon)
        update_sidebar_buttons()

    def spawn_node(name, icon):
        # Random offset between 10 and 20 pixels, converted to relative values based on the visual frame size
        offset_x = random.randint(-10, 10) / visual_frame.winfo_width()
        offset_y = random.randint(-10, 10) / visual_frame.winfo_height()

        # Create a new DraggableNode instance in the center of the visual frame, with random offset
        relx = 0.5 + offset_x
        rely = 0.5 + offset_y

        node = DraggableNode(visual_frame, name, icon, canvas)
        node.place(relx=relx, rely=rely, anchor="center")
        node_container.append(node)

    # Function to toggle expand/collapse of sub buttons
    def toggle_expand(button):
        button.toggle_expand()
        
        if button.expand_status:
            button.subbutton_frame.grid()
            button.main_button.configure(fg_color=SECONDARY_COLOR)

        else:
            button.subbutton_frame.grid_remove()
            button.main_button.configure(fg_color="transparent", hover_color=SECONDARY_COLOR)

    # Function to show a new frame on hover
    def show_frame(event, icon, name):
        subbutton = event.widget
        frame = ctk.CTkFrame(master=root, width=120, height=100, corner_radius=0, fg_color=SECONDARY_COLOR)
        frame.place(x=200 + 50, y=subbutton.winfo_rooty() - root.winfo_rooty())
        
        subbutton.hover_frame = frame

        icon_label = ctk.CTkLabel(master=frame, image=icon, text="")
        icon_label.place(relx=0.5, y = 10, anchor='n')

        name_label = ctk.CTkLabel(master=frame, text=name, font=(FONT, 12))
        name_label.place(relx=0.5, y=75, anchor='n')

    # Function to hide the new frame when hover ends
    def hide_frame(event):
        if hasattr(event.widget, 'hover_frame'):
            try:
                event.widget.hover_frame.destroy()
                event.widget.hover_frame = None
            except AttributeError:
                pass  # Tidak melakukan apa-apa jika hover_frame tidak ada


    def void_preference(event = None): 
        for widget in preference_frame.winfo_children():
            widget.destroy()
        
        title = ctk.CTkLabel(master=preference_frame, text="Preferences", font=(FONT, 16, "bold"))
        title.pack(pady=20, padx = 60)

    # Create sidebar buttons
    create_sidebar_buttons()

    # Configure grid for content area
    content.grid_columnconfigure(0, weight=1)
    content.grid_rowconfigure(2, weight=1)

    button_frame = ctk.CTkFrame(content, fg_color="#252525")
    button_frame.grid(row=1, column=0, padx=10, pady=0, sticky="ne")

    # Create frames for code and visual content
    code_frame = ctk.CTkFrame(content, fg_color=DARK_COLOR, width=300, height=300, corner_radius=0)
    visual_frame = ctk.CTkFrame(content, fg_color="#252525", width=300, height=300, corner_radius=0)

    inner_frame = tk.Frame(visual_frame, bg="#252525")
    inner_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(inner_frame, bg="#252525", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Initially show visual frame and hide code frame
    visual_frame.grid(row=2, column=0, pady=10, sticky="nsew")
    visual_frame.bind("<Button-3>", void_preference)
    code_frame.grid_remove()

    def toggle_buttons():
        global toggle_visual_or_code, text_code
        if toggle_visual_or_code:
            # If visual button is active, show visual frame and hide code frame
            visual_frame.grid(row=2, column=0, pady=0, sticky="nsew")
            code_frame.grid_remove()
            visual_button.configure(state="disabled", fg_color=ORANGE_PALLETE, text_color=DARK_COLOR)
            code_button.configure(state="normal", fg_color="#2B2B2B", text_color=TEXT_COLOR)
        else:
            void_preference()
            # If code button is active, show code frame and hide visual frame
            code_frame.grid(row=2, column=0, pady=0, sticky="nsew")
            visual_frame.grid_remove()
            code_button.configure(state="disabled", fg_color=LIGHT_GREEN_PALLETE, text_color=DARK_COLOR)
            visual_button.configure(state="normal", fg_color="#2B2B2B", text_color=TEXT_COLOR)
            
            # connection text code
            
            # reset sekaligus konfigurasi ulang
            textbox.configure(state="normal")
            textbox.delete("1.0", "end")    
            # Dapatkan gabungan semua kode dari node
            textbox.insert("end", combine_all_codes())
            highlight(textbox)
            textbox.configure(state="disabled") 

    def on_code_button_click():
        global toggle_visual_or_code
        toggle_visual_or_code = False
        toggle_buttons()

    def on_visual_button_click():
        global toggle_visual_or_code
        toggle_visual_or_code = True
        toggle_buttons()

    # Preferences Menu panel settings
    def update_preference(event, self):

        for widget in preference_frame.winfo_children():
            widget.destroy()
        
        title = ctk.CTkLabel(master=preference_frame, text="Preferences", font=(FONT, 16, "bold"))
        title.pack(pady=20, padx = 60)

        def update_info(event=None):
            self.preferences.update_data(*(val.get() for val in values))

        values = []

        for node in self.preferences.atribute():  
            if node[0] == "nama" :
                name_label = ctk.CTkLabel(master=preference_frame, text="Name", font=(FONT, 14))
                name_label.pack(pady=(0,0))
                name_entry = ctk.CTkEntry(master=preference_frame)
                name_entry.insert(0, node[1])
                name_entry.pack(pady=(0,10))
                name_entry.bind("<KeyRelease>", update_info)
                values.append(name_entry)

            elif node[0] == "framework":
                framework_label = ctk.CTkLabel(master=preference_frame, text="Framework", font=(FONT, 14))
                framework_label.pack(pady=(10,0))
                framework_combo = ctk.CTkComboBox(master=preference_frame, values=node[1], command= update_info)
                framework_combo.pack(padx=30,pady=0)
                framework_combo.set(node[2])
                values.append(framework_combo)

            elif node[0] == "link":
                link_label = ctk.CTkLabel(master=preference_frame, text="Link", font=(FONT, 14))
                link_label.pack(pady=(20, 0))
                link_entry = ctk.CTkEntry(master=preference_frame)
                link_entry.insert(0, node[1])  # Menampilkan link awal
                link_entry.pack(pady=0)
                # Event binding untuk memperbarui data setiap kali teks diubah
                link_entry.bind("<KeyRelease>", update_info)
                values.append(link_entry)

    def code_button_widget(button_frame: ctk.CTkFrame):
        code_button = ctk.CTkButton(
        master=button_frame,
        text="Code",
        width=80,
        height=30,
        corner_radius=5,
        fg_color=BACKGROUND_COLOR,
        hover_color=LIGHT_GREEN_PALLETE,
        command=on_code_button_click,
        text_color_disabled= DARK_COLOR
        )
        code_button.grid(row=0, column=0, padx=5, pady=5)

        return code_button

    code_button = code_button_widget(button_frame=button_frame)

    visual_button = ctk.CTkButton(
        master=button_frame,
        text="Visual Programming",
        width=150,
        height=30,
        corner_radius=5,
        fg_color=BACKGROUND_COLOR,
        hover_color=ORANGE_PALLETE,
        command=on_visual_button_click, 
        text_color_disabled= DARK_COLOR
    )
    visual_button.grid(row=0, column=1, padx=5, pady=5)

    def copy_code():
        pyperclip.copy(combine_all_codes())

    code_frame.grid_rowconfigure(0, weight=1)  
    code_frame.grid_columnconfigure(0, weight=1)  


    #rekrusif open gate

    def rekrusif_open_gate( node, combined_code, input = "", import_statement =[]):
        code, next, header = node.code(input)
        combined_code += code + "\n" 
        result = list(set(header + import_statement))
        #import_statement.extend([i for i in header if i not in import_statement])
        
        if node.output.next :  
            return rekrusif_open_gate(node.output.next.coor, combined_code, input=next, import_statement=result)
        else:

            return("\n\n"+'\n'.join(result) + "\n" + combined_code)

    def combine_all_codes():
        combined_code = "\n"
        if node_container :
            return rekrusif_open_gate(node_container[0], combined_code)
        else :
            return "\n\n ~~ 404 Nothing ~~"

    toggle_buttons()

    textbox = tk.Text(code_frame, width=0, height=10, bg=DARK_COLOR , fg=TEXT_COLOR, bd=0, font=(FONT, 10),tabs=("1c"))
    textbox.grid(row=0, column=0, padx = (15,0), pady = 0, sticky="nswe")

    scrollbar = ctk.CTkScrollbar(code_frame, command=textbox.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Menghubungkan scrollbar dengan textbox
    textbox.config(yscrollcommand=scrollbar.set)

    copy_button = ctk.CTkButton(
        master=code_frame,
        text="Copy",
        width=40,
        height=40,
        corner_radius=5,
        fg_color="#2B2B2B",
        hover_color=SECONDARY_COLOR,
        command=copy_code,
        image = ctk.CTkImage(light_image=Image.open(get_icon_path("copy.png")), size=(20, 20))
    )
    copy_button.grid(row=0, column=0, padx=5, pady=5, sticky="se")  # Tempelkan tombol ke pojok kanan bawah

    
    void_preference() #initial preference

    # Run the application
    root.mainloop()
    
