from ruldani_visual_programming.utils.pages.base import sidebar_class, button_sidebar, sidebar_search
import ruldani_visual_programming.utils.color_manager as cm
import customtkinter as ctk

PADDING: int = 1

class sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=170, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.hide = True
        self.toggle_widget()

    # membuat ui wiget dari sidebar
    def make_widget(self, button) -> list[ctk.CTkFrame]:
        
        sidebar_sub_btn: list[ctk.CTkFrame] = []

        # Create sidebar label
        sidebar_label = ctk.CTkLabel(
            master=self, 
            text="Connection", 
            font=(cm.FONT, 16, "bold"), 
            text_color=cm.TEXT_COLOR,
            anchor="center" 
        )
        sidebar_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="ew")

        # new side 
        new_side = sidebar_search(master=self)
        new_side.grid(row=PADDING, column=0, sticky = "ew")

        # create sidebar
        for i, title in enumerate(button) :
            
            tes = sidebar_class(master=self, text=title)
            tes.grid(row= ( 2 * i ) + PADDING + 1, column=0, padx=5, pady=5, sticky="ew") 
    
            isi_sidebar = ctk.CTkFrame(master=self, fg_color=cm.BACKGROUND_COLOR)
            isi_sidebar.grid(row= ( 2 * i ) + PADDING + 2, column=0, padx=(36,4), pady=0, sticky="we")
            isi_sidebar.grid_propagate(False)
            isi_sidebar.configure(height = 0)

            tes.bind("<Button-1>", lambda event, 
                     sidebar = isi_sidebar,
                     button = tes : 
                     self.sidebar_content_binding(sidebar= sidebar, button = button))
            
            tes.hide()
            sidebar_sub_btn.append(isi_sidebar)


        return sidebar_sub_btn
    
    # membuat sub button kedalam button ke - 1
    def make_sub_button(self, isi_sidebar:ctk.CTkFrame, icon: list, identity_btn: str, identity_sub: str, sequence: int):
        # jumlah sub button perbaris
        jumlah: int = 4

        row : int = int(sequence/jumlah)
        column : int = sequence % jumlah

        tes = button_sidebar(master=isi_sidebar, icon=icon, button=identity_btn, subbutton=identity_sub) #button, #sub button
        tes.grid(row=row, column=column, padx=0, pady=5, sticky="w")

        return tes
    
    def sidebar_content_binding(self, sidebar: ctk.CTkFrame, button: sidebar_class):
        if sidebar.grid_propagate() :
            button.hide()
            sidebar.configure(height = 0)
            sidebar.grid_propagate(False)
        
        else :
            button.show()
            sidebar.grid_propagate(True)

    def toggle_widget(self) -> None :
        if self.hide : 
            self.show()
        else :
            self.hidden()

    def hidden(self) -> None:
        self.grid_remove()
        self.hide = True
        return None

    def show(self) -> None:
        self.grid(row=0, column=0, sticky="nsw")
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        
        self.hide = False
        return None