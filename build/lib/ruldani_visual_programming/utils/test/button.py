from PIL import Image
import os
import customtkinter as ctk
from ruldani_visual_programming.utils.code_server import interpreter_code

base_dir = os.path.dirname(os.path.abspath(__file__))

def get_icon_path( filename):
    return os.path.join(base_dir, "icons", filename)

# Kelas untuk Button
class Button:
    def __init__(self, button_name, icon_button, sub_buttons=None):
        self.button_name = button_name
        self.icon_button = self._create_image(icon_button)
        self.sub_buttons = sub_buttons if sub_buttons else []
        self.expand_status = False  # Initialize expand status
        self.subbutton_frame = None  # To hold the frame for sub-buttons
        self.main_button = None

    def get_icon_path(self, filename):
        return os.path.join(base_dir, "icons", filename)
    
    def _create_image(self, icon_button):
        icon_path = get_icon_path(icon_button)
        return ctk.CTkImage(Image.open(icon_path), size=(16, 16))

    def toggle_expand(self):
        self.expand_status = not self.expand_status
    
    def toggle_expand_off(self):
        self.expand_status = False

# Kelas untuk Sub_Button
class SubButton:
    def __init__(self, sub_button_name, sub_button_icon, hover_color, input = [], output = []):
        self.sub_button_name = sub_button_name
        self.icon_path = get_icon_path(sub_button_icon)
        self.sub_button_icon = self._create_image(height=15, width=15)
        self.hover_color = hover_color
        self.interpreter = self.node_container(sub_button_name)
        self.input = self.input_node()
        self.output = self.output_node()

    def _create_image(self, height = 15 , width = 15):
        return ctk.CTkImage(Image.open(self.icon_path), size=(height, width))

    # Fungsi untuk membuat baris node 
    # Menghasilkan container dari kelas interpreter
    def node_container(self, name):
        # print(f"inisialisasi dari kelas interpreter {name}")
        return interpreter_code(name)

    # input dari kelas interpreter code
    # mengahasilkan list dari input interpreter code
    def input_node(self):
        # print(f"type input interpreter {self.sub_button_name}")
        # for n in self.interpreter.input:
        #     print(f"{n}\n")
        return self.interpreter.input

    def output_node(self):
        # print(f"type output interpreter {self.sub_button_name}")
        # for n in self.interpreter.output:
        #     print(f"{n}\n")
        return self.interpreter.output
    
if __name__ == "__main__":
    print(base_dir)