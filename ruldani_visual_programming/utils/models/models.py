from ruldani_visual_programming.utils.models.button_config import Button, SubButton
from ruldani_visual_programming.utils.models.code_identifier import code_identifier
import os

class models():
    def  __init__(self, path_configuration: str):
        self.btn: code_identifier = code_identifier(path_configuration)
        pass

    # get configuration : memuat informasi terkait button dan subbuton
    def get_configuration(self):
        return None
    
    def get_button(self) -> list[str]:
        res:list [str] = []

        for btn in self.btn.conf_button:
            res.append(btn.button_name)

        return res

    def get_sub_button(self) -> list[str]:
        res: list [list[str]] = []

        for btn in self.btn.conf_button:
            hasil: list[str] = []
            for sub in btn.sub_buttons :
                hasil.append(sub.sub_button_icon)
                print(sub.sub_button_name)
            
            res.append(hasil)
        return res

    # make new frame
    def make_new_frame(self):

        return None
    
    # preference database
    def get_preference_data():
        return None

    # ui for setting content from sidebar ( dev )
    

