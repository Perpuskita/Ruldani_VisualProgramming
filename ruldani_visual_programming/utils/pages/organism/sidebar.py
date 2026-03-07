from ruldani_visual_programming.utils.pages.atomic import sidebar_class, button_sidebar
import ruldani_visual_programming.utils.color_manager as cm
import customtkinter as ctk


class sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=170, corner_radius=0, fg_color=cm.BACKGROUND_COLOR)
        self.grid_configure()

    # membuat ui wiget dari sidebar
    def make_widget(self, button, sub_button) -> list[button_sidebar]:
        
        # jumlah sub button perbaris
        jumlah: int = 4
        sidebar_sub_btn: list[button_sidebar] = []

        # Create sidebar label
        sidebar_label = ctk.CTkLabel(
            master=self, 
            text="Connection", 
            font=(cm.FONT, 16, "bold"), 
            text_color=cm.TEXT_COLOR,
            anchor="center" 
        )
        sidebar_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="ew") 

        # create sidebar
        for i, title in enumerate(button) :
            
            tes = sidebar_class(master=self, text=title)
            tes.grid(row= ( 2 * i ) + 1, column=0, padx=5, pady=5, sticky="ew") 
    
            isi_sidebar = ctk.CTkFrame(master=self, fg_color=cm.BACKGROUND_COLOR)
            isi_sidebar.grid(row= ( 2 * i ) + 2, column=0, padx=(36,4), pady=0, sticky="we")
            isi_sidebar.grid_propagate(True)

            tes.bind("<Button-1>", lambda event, 
                     sidebar=isi_sidebar,
                     button = tes : 
                     self.sidebar_content_binding(sidebar= sidebar, button = button))

            for j, icon in enumerate(sub_button[i]) :

                row : int = int(j/jumlah)
                column : int = j % jumlah

                tes = button_sidebar(master=isi_sidebar, icon=icon, button=title, subbutton=icon) #button, #sub button
                tes.grid(row=row, column=column, padx=0, pady=5, sticky="w")

                sidebar_sub_btn.append(tes)

        return sidebar_sub_btn
    
    def sidebar_content_binding(self, sidebar: ctk.CTkFrame, button: sidebar_class):
        if sidebar.grid_propagate() :
            button.hide()
            sidebar.configure(height = 0)
            sidebar.grid_propagate(False)
        
        else :
            button.show()
            sidebar.grid_propagate(True)

    def grid_configure(self) -> None:
        self.grid(row=0, column=0, sticky="nsw")
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
