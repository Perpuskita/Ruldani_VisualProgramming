
from ruldani_visual_programming.utils.models.compiler.type_token import *
from ruldani_visual_programming.utils.models.compiler.tokens import tokens

class lexer():
    def __init__(self, text: str):
        self.token: list[tokens] = []
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
        
        return "ID"

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
            
            elif detection == "WHITE_SPACE":
                tab += 1
                write = char

            # Deteksi built in function
            elif detection != "ID":
                write = char
            
            # penambahan char string jika tidak terdeteksi
            else:
                temp = temp + char
            
            # detection tab
            if tab == 4 :
                write = "TAB"
            
            # writing new token
            if ( write != None ) or (i >= max_loop-1):

                if write == None:
                    write = "ID"

                # end token
                end = f"{line}.{i-new_l}"
                
                # penambahan token untuk yang tidak terdeteksi
                if len(temp)>0:
                    if endif:
                        end = endif
                    else:
                        end = f"{line}.{i-new_l-1}"
                    
                    # buat token baru berdasarkan variabel temp, begin dan end
                    detection_temp: str = self.type_token(temp)
                    new_token = tokens(temp, begin, end, type_token=detection_temp)
                    # new_token.print_token()

                    # append token ke token stream
                    token_stream.append(new_token)
                    begin = end
                    end = f"{line}.{i-new_l}"
                    tab = 0

                # penambahan token untuk token yang terdeteksi selain white space
                if write != " " :
                    # buat token baru berdasarkan variabel temp, begin dan end
                    new_token = tokens(write, begin, end, type_token=detection)
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

    def print_token(self):
        for token in self.token:
            token.print_token()

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
    token = lexer(analisa_biner("/path_ini_/"))
    # token.reverse()
    token.print_token()