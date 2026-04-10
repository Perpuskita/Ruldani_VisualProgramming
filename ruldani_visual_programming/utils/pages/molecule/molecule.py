import customtkinter as ctk
from ruldani_visual_programming.utils.pages.base import button_visual, button_code, textbox, button
import ruldani_visual_programming.utils.color_manager as cm


# dummy data
EXAMPLE: str = f'''pip install linux \nimport matplotlib.pyplot as plt \n{"import numpy as np\n" * 50 }'''

class head_contents(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, height= 38, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.make_widget()
        self.configure_panel()
        self.status : bool = False

    def make_widget(self)-> None:
        code_visual = button_visual(master=self)
        code_visual.grid(column = 2, row = 0, sticky = "ne", pady=4, padx=5)
        self.visual_button = code_visual

        code_code = button_code(master=self)
        code_code.grid(column = 1, row = 0, sticky = "ne", pady =4, padx = 5)
        self.code_button = code_code

        return None
    
    def switch_status(self, status):
        # jika status && status => do nothing
        # jika status != status => eksekusi
        # eksekusi
        # jika status => switch code panel
        # jika !status => switch visual panel

        if not (status and self.status) :
            if status is True :
                self.visual_button.toggle_on()
                self.code_button.toggle_off()
                self.status = True
            else :
                self.code_button.toggle_on()
                self.visual_button.toggle_off()
                self.status = False
        return None

    def configure_panel(self):
        self.grid(row=0, column =0, sticky="nsew")
        self.grid_propagate(False)
        self.columnconfigure(1, weight=1)


class code_content(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = cm.CODE_CONTENT):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color)
        self.textbox: textbox = None
        self.make_widget()
        self.make_text(EXAMPLE)

    def make_text(self, text: str) -> None:
        self.textbox.set_text(text=text)
        return None

    def make_widget(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        # make header
        # make scrollable textbox code
        self.textbox = textbox(master=self)
        self.textbox.grid(row=0, column=0, sticky="nsew")

        # make copy button frame
        copy_button_frame: ctk.CTkFrame = ctk.CTkFrame(master= self, height=60, fg_color=cm.CODE_CONTENT)
        copy_button_frame.grid(row=1, column=0, sticky="sew")
        copy_button_frame.grid_columnconfigure(0, weight=1) 
        copy_button_frame.grid_propagate(False)

        # make copy button
        self.copy_button: button = button(master=copy_button_frame, icon="copy.png", size=20, 
                                  colour=cm.SECONDARY_COLOR, 
                                  hover_colour=cm.GREEN_PALLETE)
        
        self.copy_button.grid(row=0, column=2, sticky="e", padx=(5, 10), pady=10)

        # make zoom in button
        self.zoom_in: button = button( master=copy_button_frame, icon="ZoomIn.png", size=20,
                          colour=cm.SECONDARY_COLOR, 
                          hover_colour=cm.ORANGE_PALLETE)
        
        self.zoom_in.grid_configure(row=0, column=1, sticky="e", padx=5, pady=14)
        self.zoom_in.bind("<Button-1>", lambda event : self.zoom_in_binding())


        # make zoom out button
        self.zoom_out: button = button( master=copy_button_frame, icon="ZoomOut.png", size=20,
                          colour=cm.SECONDARY_COLOR, 
                          hover_colour=cm.BLUE_PALLETE)
        
        self.zoom_out.grid_configure(row=0, column=0, sticky="e", padx=5, pady=14)
        self.zoom_out.bind("<Button-1>", lambda event : self.zoom_out_binding())

        return None
    
    def zoom_in_binding(self) -> None:
        self.textbox.zoom_in()
        self.zoom_toggle()
        return None
    
    def zoom_out_binding(self) -> None:
        self.textbox.zoom_out()
        self.zoom_toggle()
        return None

    def zoom_toggle(self) -> None:
        if self.textbox.zoom < 14:
            self.zoom_out.actived()
            self.zoom_in.deactived()

        elif self.textbox.zoom == 14:
            self.zoom_in.deactived()
            self.zoom_out.deactived()

        else:
            self.zoom_out.deactived()
            self.zoom_in.actived()

        return None
    
    def tes(self):
        print("ks")
        return

    def code_preview(self):
        # loop + make widget
        # highlight sintaks

        # show
        return None

class visual_content(ctk.CTkCanvas):
    def __init__(self, master):
        super().__init__(master, bg = cm.VISUAL_CONTENT, highlightthickness = 0)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        print(event.height) 
