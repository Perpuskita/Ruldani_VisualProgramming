import customtkinter as ctk
from ruldani_visual_programming.utils import image
from ruldani_visual_programming.utils import color_manager as cm

class sidebar_class(ctk.CTkButton):
    def __init__(self, master, text: str ):
        self.dropdown: ctk.CTkImage = image("arrow_down.png", [16, 16])
        self.hidden: ctk.CTkImage = image("arrow_right.png", [16, 16])
        
        super().__init__(master, width=120, height=10, image=self.dropdown, text=text, fg_color=cm.BACKGROUND_COLOR, hover_color=cm.SECONDARY_COLOR, font=("Concolas", 12, "normal"), anchor="w" )
    
    def hide(self) -> None:
        self.configure(image = self.hidden)

    def show(self) -> None:
        self.configure(image = self.dropdown)

class sidebar_frame(ctk.CTkFrame):
    def __init__ (self, master, ):
        super.__init__(master, width=120)

    def hide(self) -> None:
        self.configure(height = 0)
        self.grid_propagate(False)
        return None

    def show(self) -> None:
        self.grid_propagate(True)
        return None
    
class sidebar_search(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # Perbaikan: super() harus dipanggil dengan benar dan menerima master
        super().__init__(master, **kwargs)
        
        # Konfigurasi frame (misalnya lebar dan warna)
        self.configure(width=200, height=100, fg_color="transparent")
        
        # Memanggil fungsi untuk membuat widget
        self.make_widget()

    def make_widget(self):
        # 1. Membuat Input (Entry)
        self.search_entry = ctk.CTkEntry(
            self, 
            placeholder_text="Cari sesuatu...", 
            width=180,
            height=30
        )
        self.search_entry.pack(pady=(10, 5), padx=10, fill="x")
        self.search_entry.bind("<KeyRelease>", lambda event: self.on_search_click())

    def on_search_click(self):
        # Fungsi ini akan dijalankan saat tombol ditekan
        query = self.search_entry.get()
        print(f"Mencari: {query}")
        # Di sini Anda bisa menambahkan logika pencarian Anda