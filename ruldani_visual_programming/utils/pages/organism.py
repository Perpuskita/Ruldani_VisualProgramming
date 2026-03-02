import customtkinter as ctk
from ruldani_visual_programming.utils.pages import button_ribbon, preference_dropdown, preference_error, preference_text, button, sidebar_class, button_visual, button_code
import ruldani_visual_programming.utils.color_manager as cm

class ribbon(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=1080, height=30, fg_color=cm.BACKGROUND_COLOR )
        self.initial_state()
        self.grid_configure()

    def initial_state(self) -> None:
        text_title: list = ["save", "load", "tools", "view"]

        for i, title in enumerate(text_title):
            padx: int = 5
            if i == 0 :
                padx = 4
                
            btn_home = button_ribbon(master=self, text=title)
            btn_home.grid(row=0, column=i, pady=5, padx=(padx, 2), sticky="w")

        self.grid_columnconfigure(len(text_title), weight=1) 

        tes = button(master=self, icon="help.png")
        tes.grid(column=len(text_title) + 1, row=0, pady = 0, padx = 0, sticky="ns" )
    
    def grid_configure(self) -> None:
        self.grid(row=0, column=1, sticky="ew", padx=0, pady=0)
        self.grid_propagate(False)

class sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=200, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.make_widget()
        self.grid_configure()

    # membuat ui wiget dari sidebar
    def make_widget(self) -> None:
        
        # Create sidebar label
        sidebar_label = ctk.CTkLabel(
            master=self, 
            text="Connection", 
            font=(cm.FONT, 16, "bold"), 
            text_color=cm.TEXT_COLOR,
            anchor="center" 
        )

        sidebar_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="ew")  # 4. Label mengisi lebar kolom
        
        # make content sidebar
        title_contents = ["neural network", "convolutional NN"]
        icon_content_1 = ["undo.png", "undo.png", "undo.png", "undo.png", "undo.png", "undo.png"]

        for i, title in enumerate(title_contents) :
            
            tes = sidebar_class(master=self, text=title)
            tes.grid(row= ( 2 * i ) + 1, column=0, padx=5, pady=5, sticky="ew")  # 4. Label mengisi lebar kolom
    
            isi_sidebar = ctk.CTkFrame(master=self, fg_color=cm.BACKGROUND_COLOR)
            isi_sidebar.grid(row= ( 2 * i ) + 2, column=0, padx=(36,4), pady=0, sticky="we")

            isi_sidebar.grid_propagate(True)

            for j, icon in enumerate(icon_content_1) :

                row : int = int(j/4)
                column : int = j % 4

                tes = button(master=isi_sidebar, icon=icon)
                tes.grid(row=row, column=column, padx=0, pady=5, sticky="w")

    
    def grid_configure(self) -> None:
        self.grid(row=0, column=0, sticky="nsw")
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

class content(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, corner_radius=0, fg_color=cm.SECONDARY_COLOR)
        self.make_widget()
        self.configure_panel()
        pass

    def make_widget(self) -> None:
        head = ctk.CTkFrame(master=self, height=40, width=100, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        head.grid(row=0, column =0, sticky="nsew")
        head.grid_propagate(False)

        body = ctk.CTkFrame(master=self, height=30, width=100, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        body.grid(row=1, column =0, sticky="nsew")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        code_visual = button_visual(master=head)
        code_visual.grid(column = 2, row = 0, sticky = "ne", pady=4, padx=5)

        code_code = button_code(master=head)
        code_code.grid(column = 1, row = 0, sticky = "ne", pady =4, padx = 5)

        head.columnconfigure(1, weight=1)
        return None

    def configure_panel(self) -> None:
        self.grid(row=0, column=1, sticky="nsew")

class setting(ctk.CTkFrame):
    def __init__(self):
        pass

class preference(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=200, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
    
    def make_widget(self):
        tes = preference_text(master=master, text="nama node")
        tes.grid(row =1, column=0, sticky = "ew", padx = 20, pady=[20,0])
        result = preference(master=master)
        result.grid(row=2, column=0, padx=20, pady=10, sticky ="w")
        tes = preference_error(master=master, text="yahh error !")
        tes.grid(row =3, column=0, sticky = "ew", padx = 20)

        tes = preference_text(master=master, text="dropdown node")
        tes.grid(row =4, column=0, sticky = "ew", padx = 20, pady=[10,0])
        pilihan: list[str] = ["yus", "pos", "los"]
        ops = preference_dropdown(master=master, values=pilihan)
        ops.grid(row =5, column=0, sticky = "ew", padx = 20, pady = 10)

        master.grid_rowconfigure(6, weight=1)

        tes = button_ribbon(master=master, text="delete")
        tes.grid(row =7, column=0, sticky = "ew", padx = 20, pady=[0,10])


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

