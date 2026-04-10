from ruldani_visual_programming.utils.models.code_database import interpreter, code_server
from ruldani_visual_programming.utils import image


# Kelas untuk Sub_Button
class SubButton:
    def __init__(self, sub_button_name: str, sub_button_icon:str, hover_color: str):
        self.sub_button_name = sub_button_name
        self.sub_button_icon = sub_button_icon
        self.hover_color = hover_color
        self.code_server = code_server()
        self.input = None
        self.output = None
        self.text = ""

    def create_image(self, icon: str, height = 15 , width = 15):
        return image(icon, dimension=[16, 16])
    
    def text_code(self, text: str) -> None:
        self.text = text
        return None
    
    def get_text(self):
        res: str = "def " + self.sub_button_name
        return self.text

    # Fungsi untuk membuat baris node 
    # Menghasilkan container dari kelas interpreter
    def set_interpreter(self, node: interpreter) -> None:
        # print(f"inisialisasi dari kelas interpreter {name}")
        self.code_server = node
        return None

    # input dari kelas interpreter code
    # mengahasilkan list dari input interpreter code
    def input_node(self):
        # print(f"type input interpreter {self.sub_button_name}")
        # for n in self.interpreter.input:
        #     print(f"{n}\n")
        return self.code_server.input

    def output_node(self):
        # print(f"type output interpreter {self.sub_button_name}")
        # for n in self.interpreter.output:
        #     print(f"{n}\n")
        return self.code_server.output
    
# Kelas untuk Button
class Button:
    def __init__(self, button_name: str, icon_button: str):
        self.button_name: str = button_name
        self.icon_button: image = self.create_image(icon_button)
        self.sub_buttons: list[SubButton] = []
        self.expand_status = False  # Initialize expand status
        self.subbutton_frame = None  # To hold the frame for sub-buttons
        self.main_button = None
    
    def set_sub_buttons(self, test: SubButton):
        self.sub_buttons.append(test)
        # print(f"sub{test.sub_button_name}")
        return None

    def create_image(self, icon_button):
        return image(icon_button, [16,16])

    def toggle_expand_on(self):
        self.expand_status = True
    
    def toggle_expand_off(self):
        self.expand_status = False
    
if __name__ == "__main__":
    print("woke nanti di test")