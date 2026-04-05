# peghubung dan pemisah antar token
NEW_LINE = [
    "\r", "\n"
]

WHITE_SPACE = [
    " "
]

SEPARATOR = [
    "(", ")", "[", "]", "{", "}"
]

FUNC = [
    ".", ",","'",'''"''',":"
]

BUILT_IN_FUNCTION = [
    "print", "len", "range", "if", "else", "elif", "for", "return", "def", 
    "class", "import", "from", "as", "in", "#", "is","pass","self", "->", 
    "try", "except","raise", "with", "and", "or"
]

OPERATOR = [
    "+", "-", "*", "/", "//", "%", "**",
    "==", "!=", ">", "<", ">=", "<=","="
]

class token():
    def __init__(self, name, begin: int = 1, end: int = 1):
        self.name   = name
        self.begin  = begin
        self.end    = end
        self.type   = self.type_token()
        self.priority = 1
        # self.print_token()

    def detection(self, char, DEF):
        for separate in DEF:
            if char == separate:
                return separate
        return False
    
    def type_token(self):
        char = self.name
        # Type newline
        if self.name == "NEW_LINE":
            return "NEW_LINE"
        
        # Type function
        elif self.detection(char=char, DEF= FUNC):
            # print("titik atau koma")
            return "FUNC"
        
        # Type built in function 
        elif self.detection(char=char, DEF= BUILT_IN_FUNCTION):
            return "BUILT_IN_FUNCTION"
        
        # Type operator
        elif self.detection(char=char, DEF= OPERATOR):
            return "OPERATOR"
        
        # Type braces
        elif self.detection(char=char, DEF= SEPARATOR):
            return "SEPARATOR"
        
        elif char == "TAB":
            return "TAB"

        return "ID"
    
    def get_token(self):
        return self.name, self.begin, self.end, self.type

    def get_name(self):
        return self.name
    
    def print_token(self):
        name = ""
        
        # Nama untuk print token 
        if len(self.name) <= 9:
            name = f"{self.name}{' '*(9-len(self.name))}"
        else:
            name = f"{self.name[:7]}.."
        
        # print token
        print(f'''__ token : {name} ->    berada di : "{self.begin}","{self.end}" \tjenis token : {self.type}''')

class tokenizer():
    def __init__(self, text: str):
        self.token: list[token] = []
        self.token = self.make_token(text)

    def detection(self, char, DEF):
        for separate in DEF:
            if char == separate:
                return separate
        return False
    
    def type_token(self, char):
        # Type newline
        if self.detection(char=char, DEF= NEW_LINE):
            return "NEW_LINE"
        
        # Type function
        elif self.detection(char=char, DEF= FUNC):
            # print("titik atau koma")
            return "FUNC"
        
        # Type built in function 
        elif self.detection(char=char, DEF= BUILT_IN_FUNCTION):
            return "BUILT_IN_FUNCTION"
        
        # Type operator
        elif self.detection(char=char, DEF= OPERATOR):
            return "OPERATOR"
        
        # Type braces
        elif self.detection(char=char, DEF= SEPARATOR):
            return "SEPARATOR"
        
        # Type white space
        elif self.detection(char=char, DEF= WHITE_SPACE):
            return "WHITE_SPACE"
        
        return None

    # tokenisasi token
    def make_token(self, text: str):
        temp = ""
        tab = 0
        line = 1
        new_l = -1
        token_stream = []
        begin = "1.0"
        end = "1.0"

        max_loop: int = len(text)

        # loop token berdasarkan teks
        for i, char in enumerate(text) :
            write = None
            detection = self.type_token(char)
            endif = None

            # Deteksi newline \r dan \n
            if detection == "NEW_LINE":
                endif = f"{line}.{i-new_l-1}"
                line = line + 1
                new_l = i  
                write = "NEW_LINE"

            # Deteksi titik(.) dan koma (,)
            elif detection == "FUNC":
                # print(temp)
                write = char
            
            # Deteksi built in function
            elif detection == "BUILT_IN_FUNCTION":
                write = char
            
            # Deteksi Operasi
            elif detection == "OPERATOR":
                write = char
            
            # Deteksi white space
            elif detection == "WHITE_SPACE":
                tab = tab + 1
                write = " "

            # Deteksi semicolon dan braces ([, ], {, })
            elif detection == "SEPARATOR" :
                write = char

            # penambahan char string jika tidak terdeteksi
            else:
                temp = temp + char
            
            # detection tab
            if tab == 4 :
                write = "TAB"
            
            # writing new token
            if ( write != None ) :
                # end token
                end = f"{line}.{i-new_l}"
                
                # penambahan token untuk yang tidak terdeteksi
                if len(temp)>0:
                    if endif:
                        end = endif
                    else:
                        end = f"{line}.{i-new_l-1}"
                    
                    # buat token baru berdasarkan variabel temp, begin dan end
                    new_token = token(temp, begin, end)
                    # new_token.print_token()

                    # append token ke token stream
                    token_stream.append(new_token)
                    begin = end
                    end = f"{line}.{i-new_l}"
                    tab = 0

                # penambahan token untuk token yang terdeteksi selain white space
                if write != " " :
                    # buat token baru berdasarkan variabel temp, begin dan end
                    new_token = token(write, begin, end)
                    # new_token.print_token()

                    # append token ke token stream
                    token_stream.append(new_token)
                    tab = 0                    
                
                # reset variabel
                temp = ""
                begin = f"{line}.{i-new_l}"
                end = None

        # if lagi

        return token_stream
    
    def reverse(self):
        concat: str = ""
        for token in self.token:
            name: str = token.get_name()
            if  name == "NEW_LINE":
                concat += "\n"

            elif name == "TAB":
                concat += "\t"

            else :
                concat += name

            concat += " "
        
        print(concat)

if __name__ == "__main__":
    def analisa_biner(path) :
        return f'''
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


# baris untuk open folder 
folder: str = '/content/test'

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
    
    concat: str = ''''''
    token = tokenizer(analisa_biner("/path_ini_/"))
    token.reverse()