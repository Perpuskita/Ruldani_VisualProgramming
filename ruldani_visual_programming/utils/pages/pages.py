from ruldani_visual_programming.utils.pages.organism import ribbon, sidebar, content, settings, preferences
from ruldani_visual_programming.utils.pages.base import button_sidebar, nodeberzier

import customtkinter as ctk
import tkinter as tk
from ruldani_visual_programming.utils.presenters import presenters


class pages(tk.Tk):
    def __init__(self):
        super().__init__()
        self.presenter: presenters = None
        self.activate_line = None
        self.nodeberzier_container = None

    def run(self):
        # get presenter button, sub button via initial state
        button: list = self.presenter.initial_button()
        sub_button: list = self.presenter.initial_subbutton()

        # pisahkan logika pembuatan window dengan pembuatan sidebar button
        self.make_window([1440, 720])

        # membuat sidebar button
        btn: list  = self.sidebars.make_widget(button=button)
        
        sub_btn: list = []
        # gunakan loop untuk binding sidebar
        for i in range(len(btn)) :
            for j, sub in enumerate(sub_button[i]):
                new = self.sidebars.make_sub_button(isi_sidebar=btn[i], icon=sub, identity_btn= button[i], identity_sub=sub, sequence=j)
                self.binding_sidebar(new)
        
    # set presenter untuk melakukan komunikasi 2 arah ke presenter
    def set_presenter(self, presenter: presenters):
        self.presenter = presenter
        return None

    def make_window(self, geometry:list[int]) -> None:

        width = geometry[0]
        height = geometry[1]

        self.geometry(f"{width}x{height}")
        self.title("Ruldani - Visual Programming")
        
        # Configure columns and rows to allow resizing
        self.grid_rowconfigure(0, weight=1)

        # configure workspace grid configure
        self.grid_columnconfigure(0, weight= 0)
        self.grid_columnconfigure(1, weight= 1)
        
            
        # make 2 panel : panel settings and main panel
        main_panel = self.main_paneling()
        setting = settings(self)
        

        # make workspace and menubar on main panel
        workspace = self.workspace_paneling(master=main_panel)
        menubar = ribbon(master=main_panel)
        
        # workspace panel
        self.sidebars: sidebar = sidebar(master=workspace)
        self.contents = content(master=workspace)
        self.preferences = preferences(master=workspace)
        
        # binding hide sidebar
        setting.buttons[0].bind("<Button-1>", lambda event : self.hide_sidebar())
    
    def hide_sidebar(self):
        print("hide")
        self.sidebars.toggle()

    # binding sidebar dengan menggunakan lambda str 
    def binding_sidebar(self, sub_button: button_sidebar):
        sub_button.bind("<Button-1>", lambda event : self.make_visual_programming())
        return None
    
    def make_line(self):
        return None

    # make visual programming dan berikan konfigurasinya dari presenter dngan value str
    def make_visual_programming(self):

        # ambil konfigurasi dari presenter
        self.presenter.make_visual_programming()

        # buatkan visual programming content berdasarkan presenter
        self.contents.make_visual_programming()

    def clear_preferences(self):
        return None

    # make workspace panel
    def workspace_paneling(self, master):
        workspace = ctk.CTkFrame(master=master, corner_radius=0)
        workspace.grid(row=1, column=1, sticky="nsew")
        workspace.grid_columnconfigure(0, weight=0)
        workspace.grid_columnconfigure(1, weight=1)
        workspace.grid_columnconfigure(2, weight=0)
        workspace.grid_rowconfigure(0, weight=1)

        return workspace

    def main_paneling(self):
        main = ctk.CTkFrame(self, corner_radius=0)
        main.grid(row=0, column=1, sticky="nsew")
        main.grid_columnconfigure(0, weight=0)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(1, weight=1)
        return main