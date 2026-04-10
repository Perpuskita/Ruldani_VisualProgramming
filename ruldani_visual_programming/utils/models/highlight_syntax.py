
import ruldani_visual_programming.utils.color_manager as cm
from ruldani_visual_programming.utils.models.compiler import lexer
import customtkinter as ctk

ORANGE_PALLETE = cm.ORANGE_PALLETE
YELLOW_PALLETE = cm.YELLOW_PALLETE
RED_PALLETE = cm.RED_PALLETE
LIGHT_GREEN_PALLETE = cm.RED_PALLETE
GREEN_PALLETE = cm.GREEN_PALLETE
BLUE_PALLETE = cm.BLUE_PALLETE
CYAN_PALLETE = cm.CYAN_PALLETE
GRAY_PALLETE = cm.GRAY_PALLETE

# non pallete colour
BACKGROUND_COLOR = cm.BACKGROUND_COLOR
TEXT_COLOR = cm.TEXT_COLOR
DARK_COLOR = cm.DARK_COLOR
SECONDARY_COLOR = cm.SECONDARY_COLOR


# Keyword
keywords = [
    "if", "else", "elif", "for", "return", "def", 
    "class", "import", "from", "as", ":", ","
]

# OLD
TYPE_TOKEN = [
    "ID", "SEPARATOR", "BUILT_IN", "OPERATOR", "FUNC", "BUILT_IN_FUNCTION"
]

COLOR_TOKEN = [
    GRAY_PALLETE, ORANGE_PALLETE, BLUE_PALLETE, RED_PALLETE, RED_PALLETE, BLUE_PALLETE
]

# class highlight
class highlight ():

    def __init__(self, text: str, textbox: ctk.CTkTextbox):
        self.textbox = textbox
        self.raw_text = text
        self.token: lexer = lexer(self.raw_text)
        self.highlight_token()

    def highlight_token(self ):
        # memasukan text kedalam textbox        
        self.textbox.insert("end", text=self.raw_text)

        # mendapatkan semua hasil token yang sudah di olah di lexer
        profil = self.token.token

        # configurasi sementara sebelum melakukan parser
        for i, types in enumerate(TYPE_TOKEN):
            self.textbox.tag_config(types, foreground=COLOR_TOKEN[i])

        # highlight text
        for token in profil:
            name, begin, end, types = token.get_token()
            if types != "NEW_LINE" :
                # print(name + " " +begin + " " + end)
                self.textbox.tag_add(types, begin, end)
        
    def treesitter(self) -> None:
        return None