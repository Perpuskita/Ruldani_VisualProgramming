import customtkinter as ctk
import ruldani_visual_programming.utils.color_manager as cm
from ruldani_visual_programming.utils.pages.base import preference_dropdown, preference_error, preference_text, preference, preferences_connection_status, preferences_connection_name


class preferences_entry(ctk.CTkFrame):
    def  __init__(self, master, nama_widget: str = "nama_widget"):
        super().__init__(master= master, width=200, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.error: preference_error = None
        self.make_widget(nama= nama_widget)
        self.hide_error()

    # Membuat widget baru untuk teks, input node, dan error
    def make_widget(self, nama: str):
        tes = preference_text(master=self, text=nama)
        tes.grid(row =0, column=0, sticky = "ew", padx = 20, pady=[20,0])
        result = preference(master=self)
        result.grid(row=1, column=0, padx=20, pady=10, sticky ="w")
        self.error = preference_error(master=self)
        return None
    
    def show_error(self, message: str):
        self.error.configure(text= message)
        self.error.grid(row =2, column=0, sticky = "ew", padx = 20)
        return None
    
    def hide_error(self):
        self.error.grid_remove()
        return None
    

class preference_dropdown_entry(ctk.CTkFrame):
    def  __init__(self, master, nama: str, choice: list[str]):
        super().__init__(master= master, width=200, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.dropdown_entry: preference_dropdown = None
        self.error: preference_error = None
        self.make_widget(nama_node=nama, choice=choice)
    
    def make_widget(self, nama_node: str, choice: list[str]) -> None:
        tes = preference_text(master=self, text=nama_node)
        tes.grid(row =0, column=0, sticky = "ew", padx = 20, pady=[10,0])
        ops = preference_dropdown(master=self, values=choice)
        ops.grid(row =1, column=0, sticky = "ew", padx = 20, pady = 10)
        self.error = preference_error(master=self)
        return None
    
    def show_error(self, message: str):
        self.error.configure(text= message)
        self.error.grid(row =2, column=0, sticky = "ew", padx = 20)
        return None
    
    def hide_error(self):
        self.error.grid_remove()
        return None
    
class preference_connection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=30, fg_color=cm.SECONDARY_COLOR)
        self.grid(padx=10, pady= 10)
        self.make_widget()

    def make_widget(self) -> None :
        # make a number => 01
        number: ctk.CTkLabel = ctk.CTkLabel(master=self, text="01", width=20, height=20, fg_color=cm.SECONDARY_COLOR)
        number.grid(column=0, row=0, padx=5, pady=5, sticky="w")

        # make a nama connection: preference conn textbox => Nama_panel.connection_var
        connection_name: preferences_connection_name = preferences_connection_name(master=self, nama_node="koel", connection_name="koe")
        connection_name.grid(column=1, row=0, padx=5, pady=2, sticky="we")

        # make a next connection: preference conn status => kotak + warna + status + kemana ?
        status:preferences_connection_status = preferences_connection_status(master=self)
        status.grid(column=1, row=1, padx=5, pady=2, sticky="we")

        return None
    
    def on_click(self) -> None:
        return None
    
class preference_connection_drawer(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200):
        super().__init__(master, width, height, fg_color=cm.BACKGROUND_COLOR)
        self.hide = False
        self.height_header: int = 20
        
        self.make_widget()
        self.toggle_widget()
        
    def widget_counter(self):
        return None

    def make_widget(self) -> None:
        # configure grid propagate
        self.grid_propagate(False)
        
        # make swipe header
        header = ctk.CTkLabel(master=self, text="Connection Review", 
                              height=self.height_header, 
                              width=200, 
                              fg_color=cm.SECONDARY_COLOR, 
                              text_color=cm.TEXT_COLOR, 
                              corner_radius=6)
        
        # header grid configure
        header.grid_configure(column=0, row=0)
        
        # binding header widget
        header.bind("<Button-1>", lambda event: self.toggle_widget())

        # make connection
        return None

    def toggle_widget(self) -> None:
        print("toggle widget")
        if self.hide :
            self.show_widget()

        else:
            self.hide_widget()

        self.hide = not self.hide
        return None

    def expose_widget(self) -> None:
        return None

    def hide_widget(self) -> None:
        self.configure(height=self.height_header)
        return None
    
    def show_widget(self) -> None:
        self.configure(height=200)
        return None