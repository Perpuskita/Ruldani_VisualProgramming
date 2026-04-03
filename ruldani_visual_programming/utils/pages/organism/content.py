import customtkinter as ctk
from ruldani_visual_programming.utils.pages.molecule import head_contents, visual_content, code_content, visual_programming_frame
import ruldani_visual_programming.utils.color_manager as cm
from ruldani_visual_programming.utils.pages.base import preferences_hidden_button

class content(ctk.CTkCanvas):
    def __init__(self, master):
        super().__init__(master=master)
        self.make_widget()
        self.configure_panel()
        self.visual_mode = False
        self.bind("<Configure>", self.on_resize)
        self.node_container: list = []
        self.active_line = None
        self.visual_frame_container: list [visual_programming_frame] = []
        
        # futureproof
        # self.hidden_preferences = None

    def make_widget(self) -> None:
        self.head = head_contents(master=self)
        self.binding_head_button(self.head)

        body = ctk.CTkFrame(master=self, height=30, width=100, corner_radius=0, fg_color=cm.DARK_COLOR)
        body.grid(row=1, column =0, sticky="nsew")

        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)
        
        self.code_content = code_content(master=body, corner_radius=0)
        self.visual_content = visual_content(master=body)

        # membuat pref hidden button
        self.pref_hiden: preferences_hidden_button = preferences_hidden_button(master=self.visual_content)
        self.pref_hiden.place(relx = 1, rely = 0.1, anchor = "ne" )

        # make status on visual frame at first
        self.switch_content(status="visual")


        return None
    
    def toggle_preference(self)-> None:
        self.pref_hiden.toggle()
        return None

    def binding_head_button(self, head: head_contents):
        self.head.code_button.bind("<Button-1>", lambda event : self.switch_content(status="code"))
        self.head.visual_button.bind("<Button-1>", lambda event : self.switch_content(status="visual"))
        return None

    def make_visual_programming(self) -> bool:
        if not self.head.status:
            return False
        new: visual_programming_frame = visual_programming_frame(master=self.visual_content, text="mainframe", container=self.node_container, active_line=self.active_line)
        self.visual_frame_container.append(new)
        return True
    
    def on_resize(self, event):
        self.after(50, self.update_node)
        
    def update_node(self):
        for frame in self.visual_frame_container :
            frame.update_node()

    def switch_content(self, status: str):
        if (status == "visual") :
            self.visual_content.grid_configure(row=0, column=0, padx=0, pady=0, sticky="nsew")
            self.code_content.grid_remove()
            self.head.switch_status(True)
            self.on_resize(event=None)

        if (status == "code" ) :
            self.code_content.grid_configure(row=0, column=0, padx=0, pady=0, sticky="nsew")
            self.visual_content.grid_remove()
            self.head.switch_status(False)
            

    def configure_panel(self) -> None:
        self.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)