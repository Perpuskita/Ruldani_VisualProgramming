import customtkinter as ctk
from ruldani_visual_programming.utils.pages.atomic import preference_dropdown, preference_error, preference_text, preference
import ruldani_visual_programming.utils.color_manager as cm


class preferences(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=200, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.make_widget()
        self.configure_panel()

    def make_widget(self):
        tes = preference_text(master=self, text="nama node")
        tes.grid(row =1, column=0, sticky = "ew", padx = 20, pady=[20,0])
        result = preference(master=self)
        result.grid(row=2, column=0, padx=20, pady=10, sticky ="w")
        tes = preference_error(master=self, text="yahh error !")
        tes.grid(row =3, column=0, sticky = "ew", padx = 20)

        tes = preference_text(master=self, text="dropdown node")
        tes.grid(row =4, column=0, sticky = "ew", padx = 20, pady=[10,0])
        pilihan: list[str] = ["yus", "pos", "los"]
        ops = preference_dropdown(master=self, values=pilihan)
        ops.grid(row =5, column=0, sticky = "ew", padx = 20, pady = 10)


    def configure_panel(self):
        self.grid(row=0, column=2, sticky="ns")
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        
        # menambahkan label
        preference_label = ctk.CTkLabel(
            self, 
            text="Preference", 
            font=(cm.FONT, 16, "bold"), 
            text_color=cm.TEXT_COLOR,
            anchor="center" 
        )

        preference_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")  # 4. Label mengisi lebar kolom

