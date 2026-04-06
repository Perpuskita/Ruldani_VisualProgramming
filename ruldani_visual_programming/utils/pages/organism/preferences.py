import customtkinter as ctk
from ruldani_visual_programming.utils.pages.molecule import preferences_entry, preference_dropdown_entry, preference_connection_drawer
import ruldani_visual_programming.utils.color_manager as cm


class preferences(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=200, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.counter: int = 0               # membuat penghitung widget 
        self.hidden_status: bool = True     # status hidden utuk widget
        self.configure_panel()              # konfigurasi untuk panel
        self.toggle_widget()                # non aktifkan widget untuk pertama kali

    # penghitung widget
    def widget_counter(self):
        self.counter += 1 
        return self.counter

    def make_widget(self) -> None:
        
        # label preferences
        self.preference_label = ctk.CTkLabel(
            self, 
            text="Preference", 
            font=(cm.FONT, 16, "bold"), 
            text_color=cm.TEXT_COLOR,
            anchor="center" 
        )

        self.preference_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")  
        return None

    def custom_widget(self) -> None:
        # widget 1
        sop: preferences_entry = preferences_entry(master=self, nama_widget= "nama_node")
        sop.grid(row = self.widget_counter(), column=0, sticky="ew")

        # widget 2
        pilihan: list[str] = ["yus", "pos", "los"]
        sep: preference_dropdown_entry = preference_dropdown_entry(master=self, nama="dropdown", choice=pilihan)
        sep.grid(row = self.widget_counter(), column=0, sticky="ew")

        # widget space
        self.grid_rowconfigure(index= self.widget_counter(), weight=1)

        # connection list
        conn: preference_connection_drawer = preference_connection_drawer(master=self)
        conn.grid(row=self.widget_counter(), sticky ="ew")

        return None
        
    def configure_panel(self) -> None:
        # grid configure
        self.grid(row=0, column=2, sticky="ns")
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

        # membuat beberapa widget inti
        self.make_widget()

        return None
        
    def reset_widget(self) -> None:
        return None
    
    def set_widget(self) -> None:
        return None
    
    def toggle_widget(self) -> None:
        if self.hidden_status:
            self.hide_widget()
        else:
            self.show_widget()
        
        self.hidden_status = not self.hidden_status
        return None
    
    def show_widget(self) -> None:
        self.configure(width=200)
        self.preference_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")  
        return None
    
    def hide_widget(self) -> None:
        self.configure(width=30)
        self.preference_label.grid_remove()
        return None