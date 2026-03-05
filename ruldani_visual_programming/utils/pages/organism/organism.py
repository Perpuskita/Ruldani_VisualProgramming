import customtkinter as ctk
from ruldani_visual_programming.utils.pages.atomic import button_ribbon, preference_dropdown, preference_error, preference_text, button, sidebar_class, preference, button_sidebar
from ruldani_visual_programming.utils.pages.molecule import head_contents, visual_content, code_content, visual_programming_frame
import ruldani_visual_programming.utils.color_manager as cm

class sidebar(ctk.CTkFrame):
    def __init__(self, master, button: list, subbutton: list):
        super().__init__(master=master, width=170, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.button = button
        self.subbutton = subbutton
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
        title_contents = self.button
        icon_content = self.subbutton

        for i, title in enumerate(title_contents) :
            
            tes = sidebar_class(master=self, text=title)
            tes.grid(row= ( 2 * i ) + 1, column=0, padx=5, pady=5, sticky="ew")  # 4. Label mengisi lebar kolom
    
            isi_sidebar = ctk.CTkFrame(master=self, fg_color=cm.BACKGROUND_COLOR)
            isi_sidebar.grid(row= ( 2 * i ) + 2, column=0, padx=(36,4), pady=0, sticky="we")

            isi_sidebar.grid_propagate(True)

            for j, icon in enumerate(icon_content[i]) :

                row : int = int(j/4)
                column : int = j % 4

                tes = button_sidebar(master=isi_sidebar, icon=icon, button=title, subbutton=icon) #button, #sub button
                tes.grid(row=row, column=column, padx=0, pady=5, sticky="w")

    def binding_subbutton(self, sub_button: ctk.CTkButton):
        return None
    
    def binding_button(self):
        return None

    def grid_configure(self) -> None:
        self.grid(row=0, column=0, sticky="nsw")
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

class content(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, corner_radius=0, fg_color=cm.SECONDARY_COLOR)
        self.make_widget()
        self.configure_panel()
        self.visual_mode = False

    def make_widget(self) -> None:
        head = head_contents(master=self)
        body = ctk.CTkFrame(master=self, height=30, width=100, corner_radius=0, fg_color=cm.DARK_COLOR)
        body.grid(row=1, column =0, sticky="nsew")

        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)
        
        self.visual_content = code_content(master=body, corner_radius=0)
        self.code_content = visual_content(master=body, corner_radius=0, fg_color=cm.DARK_COLOR)

        test = visual_programming_frame(master=self.visual_content)

        self.switch_content(status="visual")

        return None

    def switch_content(self, status: str):
        if status == "visual" :
            self.visual_content.grid_configure(row=0, column=0, padx=0, pady=0, sticky="nsew")
            self.code_content.grid_remove()

        if status == "code" :
            self.code_content.grid_configure(row=0, column=0, padx=0, pady=0, sticky="nsew")
            self.visual_content.grid_remove()

    def configure_panel(self) -> None:
        self.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

class settings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master = master, width=40, fg_color = cm.BACKGROUND_COLOR, corner_radius=0)
        self.configure_panel()
        self.make_widget()

    def make_widget(self) -> None:
        img: list[str] = ["thumbnail_bar.png","cpm1.png", "cpm2.png", "cpm3.png"]

        for i, image in enumerate(img):
            atomic = button(master=self, icon=image)
            if i == 0 :
                atomic.grid(row=i, column=0, pady= (3, 5), padx=(5, 5), sticky="n")

            else :
                atomic.grid(row=i, column=0, pady= (5, 5), padx=(5, 5), sticky="n")

        self.grid_rowconfigure(len(img), weight=1) 

        tes = button(master=self, icon="settings.png")
        tes.grid(row=len(img) + 1, column=0, pady = 5, padx = 0, sticky="ns" )
        
        return None

    def configure_panel(self) -> None:
        self.grid(row=0, column=0, sticky="ns")
        self.grid_propagate(False)
        self.grid_columnconfigure(3, weight=1)
        return None

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

