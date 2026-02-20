if __name__ == "__main__":
    import color_manager as cm
    from lexer import lexical_analysis as lexer
    from tokenizer import tokenizer

else:
    import ruldani_visual_programming.color_manager as cm
    from ruldani_visual_programming.lexer import lexical_analysis as lexer
    from ruldani_visual_programming.tokenizer import tokenizer


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

    def __init__(self, text):
        self.textbox = text
        self.raw_text = text.get("1.0", "end")
        self.token = tokenizer(self.raw_text)
        self.lexer = lexer()
        self.highlight_token()
    
    def lexer ():

        return

    def highlight_token( self ):
        profil = self.token.token

        # configurasi sementara sebelum melakukan parser
        for i, types in enumerate(TYPE_TOKEN):
            self.textbox.tag_configure(types, foreground=COLOR_TOKEN[i])

        # highlight text
        for token in profil:
            _, begin, end, types = token.get_token()
            if types != "NEW_LINE" :
                self.textbox.tag_add(types, begin, end)
            # token.print_token()
    
if __name__ == "__main__":
    import tkinter as tk
    import os

    def read_file_to_string(file_path):
        """Membaca file text menjadi string dengan error handling"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        try:
            with open(f"{base_dir}/test/button.py", 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' tidak ditemukan")
            return None
        except Exception as e:
            print(f"Error membaca file: {e}")
            return None

    # Usage
    content = read_file_to_string('test\\button.py')

    root = tk.Tk()
    root.geometry("1080x720")
    root.configure(bg=DARK_COLOR)

    root.title("ayo semangat ngodingnya biar dpet istri cantik")

    # Membuat Textbox
    textbox = tk.Text(
        root, 
        width=0, 
        height=20, 
        bg=DARK_COLOR,
        fg= TEXT_COLOR,
        bd=0, 
        font=("Consolas", 12), 
        tabs=("1c")
    )
    textbox.pack(expand=True, fill="both")

    text = content
    # configure 
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("end", text)

    # loop pada tokenizer
    high = highlight(textbox)

    root.mainloop()