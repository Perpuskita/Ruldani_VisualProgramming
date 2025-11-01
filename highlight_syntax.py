
PRIMARY_COLOR = "#78ABA8"
ORANGE_PALLETE = "#EF9C66"
YELLOW_PALLETE = "#FCFF60"
RED_PALLETE = "#AD4C4C"
LIGHT_GREEN_PALLETE = "#C8CFA0"
SECONDARY_COLOR = "#646464"
GREEN_PALLETE = "#52B969"
BLUE_PALLETE = "#3E7BCA"
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

# peghubung dan pemisah antar token
separator = [
    " ", "\r", "\n","(", ")"
]

braces = [
    "(", ")", "[", "]", "."
]

# tipe data yang sering digunakan
data_type = [
    "int", "float", "string"
]

# Literal
literals = [
    "True", "False", "None"
]

# Operator
operators = [
    "+", "-", "*", "/", "//", "%", "**",
    "==", "!=", ">", "<", ">=", "<=","="
]

# Comment
comments = [
    "#"
]

# Built-in Functions
built_in_functions = [
    "print", "len", "range"
]

white_space = [
    " "
]

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

                # 1. Deteksi Tepi dengan Metode Canny
                edges_canny = cv2.Canny(image_np, 100, 200)

                # 2. Deteksi Tepi dengan Metode Sobel (menggunakan gradien)
                
                # Gradien di arah X
                sobel_x = cv2.Sobel(image_np, cv2.CV_64F, 1, 0, ksize=3)
                
                # Gradien di arah Y
                sobel_y = cv2.Sobel(image_np, cv2.CV_64F, 0, 1, ksize=3)
                
                # Menggabungkan gradien X dan Y
                sobel_edges = cv2.magnitude(sobel_x, sobel_y)

                # 3. Deteksi Tepi dengan Metode Laplacian
                laplacian = cv2.Laplacian(image_np, cv2.CV_64F)
                
                # Menyusun kembali hasilnya ke format gambar
                laplacian_edges = np.uint8(np.absolute(laplacian))

                # Simpan hasil deteksi tepi ke dalam daftar
                titles = [  "Gambar Asli",
                            "Deteksi Tepi Canny", 
                            "Deteksi Tepi Sobel", 
                            "Deteksi Tepi Laplacian", 
                            "Gradien Sobel X", 
                            "Gradien Sobel Y" ]
                
                images = [
                    image_np,
                    edges_canny,
                    sobel_edges,
                    laplacian_edges,
                    np.uint8(np.absolute(sobel_x)),
                    np.uint8(np.absolute(sobel_y))
                ]

                # Tampilkan hasilnya menggunakan loop
                plt.figure(figsize=(12, 8))
                for i in range(len(images)):
                    plt.subplot(2, 3, i + 1)
                    plt.imshow(images[i], cmap='gray')
                    plt.title(titles[i])
                    plt.axis('off')

                plt.tight_layout()
                plt.show()

    deteksi_tepi_folder_images('{path}')'''

class lexer_chain_text():
    def __init__(self, name, begin, end, next_chain, prev_chain):
        self.name = name
        self.begin = begin
        self.next = end
        self.next = next_chain
        self.prev = prev_chain
    
    def type(self):
        return None

# class highlight
class highlight ():

    def __init__(self, text):
        self.textbox = text
        self.parser()
        

    def lexer( self ):
        
        return
    
    def parser(self):
        # highlight normal

        for key in operators :
            self.highlight_text(key, "1.0", BLUE_PALLETE )
            
        for key in keywords :
            self.highlight_text(key, "1.0", ORANGE_PALLETE, separator_status= separator)
        
        for key in braces :
            self.highlight_text(key, "1.0", RED_PALLETE)

        for key in data_type :
            self.highlight_text(key, "1.0", RED_PALLETE, separator_status= " ")

        for key in built_in_functions :
            self.highlight_text(key, "1.0", GREEN_PALLETE, separator_status= "(")
        
        self.highlight_text("in", "1.0", GREEN_PALLETE, separator_status= " ")
        self.highlight_beetween([".", "("], "1.0", CYAN_PALLETE, [".", ")", "\n", "as"], name="cyanni")
        # self.highlight_beetween(["as", "\n"], "1.0", CYAN_PALLETE, False, name="cyan_as")
        self.highlight_beetween(["'", "'"], "1.0", YELLOW_PALLETE, name= 'tes')
        self.highlight_beetween(['''"''', '''"'''], "1.0", YELLOW_PALLETE, name= 'tes2')
        self.highlight_beetween(["#", "\n"], "1.0", GRAY_PALLETE )
        # highlight kata yang berada di dalam sebuah state
    
    def search_string( self, search_text, index ):
        return self.textbox.search(search_text, index, stopindex="end")

    def highlight_text(self, search_text, index, fr_text, separator_status = None):
                
        # Mencari teks dalam textbox satu perhuruf
        start_index = self.search_string(search_text, index)
        # print(start_index)

        # Jika tidak ditemukan, keluar dari fungsi
        if not start_index: 
            return

        # Menghitung indeks akhir dari substring yang ditemukan
        end_index = f"{start_index.split('.')[0]}.{int(start_index.split('.')[1]) + len(search_text)}"

        # Cek karakter setelah end_index
        next_index = f"{start_index.split('.')[0]}.{int(start_index.split('.')[1]) + len(search_text)}"
        next_char = self.textbox.get(next_index)  # Mendapatkan karakter di next_index

        if separator_status != None :
            for var in separator_status :
                if next_char == var :
                    # Konfigurasi tag untuk teks berwarna
                    self.textbox.tag_configure(search_text, foreground=fr_text)
                    self.textbox.tag_add(search_text, start_index, end_index)
        else :
            self.textbox.tag_configure(search_text, foreground=fr_text)
            self.textbox.tag_add(search_text, start_index, end_index)

        # Lanjutkan mencari dari posisi setelah substring terakhir yang ditemukan
        self.highlight_text(search_text, end_index, fr_text, separator_status=separator_status)
    # Highligt diantara token
    def highlight_beetween (self, search_beetween, index, fr_text, search_cancel = None, name = None):

        # Mencari teks dalam textbox satu perhuruf
        
        start_index = self.search_string(search_beetween[0], index)
        #print(start_index)
        start = start_index
        
        if not start_index:
            return 
        else :
            if search_beetween[0] == search_beetween[1] or search_cancel != None or search_cancel == False:
                start_index = f"{start_index.split('.')[0]}.{int(start_index.split('.')[1]) + len(search_beetween[0])}"

        end_index = self.search_string(search_beetween[1], start_index)
        # print(end_index)

        if search_cancel != None:
            cancelation_index = None

            if search_cancel :
                for var in search_cancel :

                    cancelation = self.search_string(var, start_index)

                    if cancelation :
                        if cancelation < end_index:
                            cancelation_index = cancelation
                            print(f"{cancelation} {end_index}")
                            break
                
            if cancelation_index == None :
                if name == None :
                    name = "search_beetween" + fr_text

                self.textbox.tag_configure(name, foreground=fr_text)
                self.textbox.tag_add(name, start, end_index)

            else :
                end_index = cancelation_index                

        else :
            if name == None :
                name = "search_beetween" + fr_text

            self.textbox.tag_configure(name, foreground=fr_text)
            self.textbox.tag_add(name, start_index, end_index)

        end_index = f"{end_index.split('.')[0]}.{int(end_index.split('.')[1]) + len(search_beetween[0])}"

        self.highlight_beetween(search_beetween, end_index, fr_text, search_cancel)
        #print("highlight between")


if __name__ == "__main__":

    import tkinter as tk

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

    # configure 
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("end", analisa_biner("/path/your_path"))

    H_TEXT = highlight(textbox)

    root.mainloop()