PRIMARY_COLOR = "#78ABA8"
ORANGE_PALLETE = "#EF9C66"
YELLOW_PALLETE = "#FCFF60"
RED_PALLETE = "#AD4C4C"
LIGHT_GREEN_PALLETE = "#C8CFA0"
SECONDARY_COLOR = "#646464"
GREEN_PALLETE = "#52B969"
BLUE_PALLETE = "#5E8FCF"
CYAN_PALLETE = "#46B1C4"

GRAY_PALLETE = "#BBBBBB" 

HOVER_COLOR = "#0056b3"
BACKGROUND_COLOR = "#343a40"
TEXT_COLOR = "#ffffff"
DARK_COLOR = "#000000"



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
        self.highlight_token()
    
    def highlight_token( self ):
        profil = self.token.token

        for i, types in enumerate(TYPE_TOKEN):
            self.textbox.tag_configure(types, foreground=COLOR_TOKEN[i])

        # highlight text
        for token in profil:
            _, begin, end, types = token.get_token()
            if types != "NEW_LINE" :
                self.textbox.tag_add(types, begin, end)
            # token.print_token()
    
if __name__ == "__main__":
    from tokenizer import tokenizer
    import tkinter as tk

    def analisa_biner(path) :
        return f'''
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


# baris untuk open folder 
folder = '/content/test'

# Fungsi untuk melakukan transformasi Fourier pada gambar dalam folder
def deteksi_tepi_folder_images(folder_path):

    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(folder_path, filename)

            # Baca gambar dan lakukan Fourier Transform
            image = Image.open(image_path).convert('L')

            # Konversi ke numpy array untuk kompatibilitas dengan cv2
            image_np = np.array(image)

deteksi_tepi_folder_images('{path}')'''

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

    text = analisa_biner("/pathini/")
    # configure 
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("end", text)

    # loop pada tokenizer
    high = highlight(textbox)

    root.mainloop()

else : 
    from src.tokenizer import tokenizer