from ruldani_visual_programming.utils.pages.organism import ribbon, sidebar, content, settings, preferences
from ruldani_visual_programming.utils.pages.atomic import button_sidebar

import customtkinter as ctk
import tkinter as tk
from ruldani_visual_programming.utils.presenters import presenters


class pages(tk.Tk):
    def __init__(self):
        super().__init__()
        self.presenter: presenters = None

    def run(self):
        # get presenter button, sub button via initial state
        button: list = self.presenter.initial_button()
        sub_button: list = self.presenter.initial_subbutton()

        self.make_window([1440, 720], button=button, subbutton=sub_button)

    # set presenter untuk melakukan komunikasi 2 arah ke presenter
    def set_presenter(self, presenter: presenters):
        self.presenter = presenter
        return None

    def make_window(self, geometry:list[int], button: list, subbutton:list) -> None:

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
        main_panel = self.main_panel()
        setting = settings(self)

        # make workspace and menubar on main panel
        workspace = self.workspace_panel(master=main_panel)
        menubar = ribbon(master=main_panel)
        
        # workspace panel
        self.sidebars: sidebar = sidebar(master=workspace)
        sub_btn: list  = self.sidebars.make_widget(button=button, sub_button=subbutton)

        self.binding_sidebar(sub_button=sub_btn)

        self.contents = content(master=workspace)
        self.preferences = preferences(master=workspace)
    
    def binding_sidebar(self, sub_button: list[button_sidebar]):
        for button in sub_button:
            button.bind("<Button-1>", lambda event : self.make_visual_programming())

        return None

    def make_visual_programming(self):
        self.contents.make_visual_programming_frame()
        self.presenter.make_visual_programming()

    def clear_preferences(self):
        return None

    # make workspace panel
    def workspace_panel(self, master):
        workspace = ctk.CTkFrame(master=master, corner_radius=0)
        workspace.grid(row=1, column=1, sticky="nsew")
        workspace.grid_columnconfigure(0, weight=0)
        workspace.grid_columnconfigure(1, weight=1)
        workspace.grid_columnconfigure(2, weight=0)
        workspace.grid_rowconfigure(0, weight=1)

        return workspace

    def main_panel(self):
        main = ctk.CTkFrame(self, corner_radius=0)
        main.grid(row=0, column=1, sticky="nsew")
        main.grid_columnconfigure(0, weight=0)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(1, weight=1)
        return main