from ruldani_visual_programming.utils.models.compiler import lexer
from ruldani_visual_programming.utils.models.code_database import code_server
from ruldani_visual_programming.utils.models.button_config import Button, SubButton


class code_identifier:
    def __init__(self, rawtext: str)-> None:
        self.raw_text = rawtext
        self.conf_button = self.get_class_name()
        self.class_name = []
        self.func_name = []
        self.lexer: lexer = None

    def get_tokenizer (self, text: str) -> lexer :
        return lexer(text=text)

    # mengambil nama class dari token yang diberikan
    def get_class_name(self) -> list[Button]:
        constrait : list = ["class", "id", "func", "id", "func", "func", "enter"]
        
        # make new tokenizer stream
        self.lexer: lexer = self.get_tokenizer(self.raw_text)
        profil = self.lexer.token
        
        # reverse token agar bisa di pop
        profil.reverse()

        res: list[Button] = []
        jump: int = 0

        len_profiler: int = len(profil)

        while len(profil) > 0:
            if jump != 0 :
                jump -= 1
                continue

            nama = profil.pop().get_name()
            if nama == "class":
                wahhid = profil.pop().get_name()
                btn_now: Button = Button(wahhid, "home.png")

                # jump to get_func_name
                sub: list[SubButton] = self.get_func_name()
                # for btn_sub in sub: 
                #     print(btn_sub.text)
                
                # memasukan sub button kedalam button
                for sub_b in sub :
                    btn_now.set_sub_buttons(sub_b) 

                res.append(btn_now)

        return res
    
    # make sub_button
    def get_func_name(self) -> list[SubButton]:
        # constrait : list = ["(", "args*", ")"]
        # pengumpul sementara 

        profil = self.lexer.token
        temp: str = None
        sub: SubButton = None
        single_tab: bool = True
        list_sub: list[SubButton] = []

        while len(profil) > 0:
            # seek untuk token berikutnya
            wahh = profil[len(profil)-1].get_name()
            
            # deteksi fungsi baru dalam token
            if wahh == "def":
                if sub :
                    sub.text_code(text=temp)

                temp = ""

                # new sub button class
                temp += profil.pop().get_name()
                nama_fun = profil.pop().get_name()

                if nama_fun == "__init__":
                    continue
                
                # pembuatan subbutton baru
                btn_sub: SubButton = SubButton(nama_fun, "add_drive.png", hover_color="#f8a4a4")
                list_sub.append(btn_sub)
                temp += " " + nama_fun
                sub = btn_sub

                # masuk ke fungsi make interpreter
                interpreter: code_server = self.get_codeserver()
                btn_sub.set_interpreter(node=interpreter)
            
            elif wahh == "class":
                # masukan kedalam interpreter yang berjalan
                return list_sub
            
            else :
                if temp :
                    res: str =  profil.pop().get_name()
                    
                    if res == "NEW_LINE" :
                        temp+= "\n"
                        single_tab = False

                    elif res == "TAB":
                        if single_tab :
                            temp += "\t"
                        else:
                            single_tab = not single_tab

                    elif res == ".":
                        temp += res
                    elif res == "(" :
                        temp +=  res
                    else:
                        if len(profil) <= 0 :
                            temp += res
                            break
                        
                        # seek next variable
                        seek: str = profil[-1].get_name()

                        # penentuan next token print
                        if res == "/":
                            temp += self.expression_helper(seek=seek, res=res, concatination = "//")

                        elif res == "*":
                            temp += self.expression_helper(seek=seek, res=res, concatination = "**")

                        elif res == "=":
                            temp += self.expression_helper(seek=seek, res=res, concatination = "==")

                        elif res == "-":
                            temp += self.expression_helper(seek=seek, res=res, concatination = "->")
                        
                        else :

                            if seek == ".":
                                temp += res

                            elif seek == ",":
                                temp += res

                            elif seek == "(" or seek == ")":
                                temp += res

                            else :
                                temp += res + " "
                else :
                    profil.pop()

        sub.text_code(text=temp)
        return list_sub
    
    def expression_helper(self, res: str, seek: str, concatination: str ) -> bool:
        # mengembalikan nilai jika res + seek == concationation
        if (res + seek) == concatination:
            return res
        
        else :
            return res + " "

    def get_codeserver(self) -> code_server:
        profile = self.lexer.token

        temp_string: str = ""

        # make new code server
        new_codeserver: code_server = code_server()

        # fungsi untuk mencari input dengan cara loop a mencari fungsi
        # loop b mencari tipedata dan preferensi
        
        while True:
            nama_var = profile.pop().get_name()
            seek = profile[-1].get_name()

            if nama_var == ")":
                break
            
            # loop b dimulai ketika menemukan : (titik dua) pada seek
            elif seek == ":" :

                # pop titik dua dari stack
                profile.pop()
                
                while True :
                    seek_token = profile[-1].get_name()
                    
                    if seek_token == "=":
                        token: str = temp_string
                        profile.pop() # mengeluarkan token =

                        value: str = profile.pop().get_name()
                        new_codeserver.make_pref(token = token, value = value)

                    elif seek_token == ")" or seek_token == ",":
                        # dilakukan input ke button input
                        new_codeserver.make_input(temp_string)
                        temp_string = ""
                        
                        break
                    
                    else :
                        temp_string += profile.pop().get_name()
            
            else:
                continue

        # fungsi untuk mencari output dengan cara loop 
        # loop mencari -> tipe data

        output: str = ""

        while True :
            token = profile.pop().get_name()
            seek = profile[-1].get_name()

            if (token + seek) == "->" :
                profile.pop()
            
            elif seek == ":":
                output += token
                break

            else:
                output += token

        new_codeserver.make_output(output)
        new_codeserver.reverse_code()

        return new_codeserver