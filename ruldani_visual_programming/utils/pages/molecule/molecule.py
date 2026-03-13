import customtkinter as ctk
from ruldani_visual_programming.utils.pages.atomic import button_visual, button_code
import ruldani_visual_programming.utils.color_manager as cm

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
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

    def make_widget(self):
        return None

class visual_content(ctk.CTkCanvas):
    def __init__(self, master):
        super().__init__(master, bg = "#2B2B2B", highlightthickness = 0)

    
