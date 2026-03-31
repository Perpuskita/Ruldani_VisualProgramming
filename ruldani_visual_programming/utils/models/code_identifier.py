from ruldani_visual_programming.utils.models.compiler import tokenizer
from ruldani_visual_programming.utils.models.code_database import interpreter
from ruldani_visual_programming.utils.models.button_config import Button, SubButton


class code_identifier:
    def __init__(self, rawtext: str)-> None:
        self.raw_text = rawtext
        self.conf_button = self.get_class_name()
        self.class_name = []
        self.func_name = []

    def get_tokenizer (self, text: str) -> tokenizer :
        return tokenizer(text=text)

    # mengambil nama class dari token yang diberikan
    def get_class_name(self) -> list[Button]:
        constrait : list = ["class", "id", "func", "id", "func", "func", "enter"]
        
        # make new tokenizer stream
        lexer: tokenizer = self.get_tokenizer(self.raw_text)
        profil = lexer.token
        
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
                sub: list[SubButton] = self.get_func_name( profil=profil)
                
                # memasukan sub button kedalam button
                for sub_b in sub :
                    btn_now.set_sub_buttons(sub_b) 
                    # print(sub_b.text)

                res.append(btn_now)

        return res
    
    # make sub_button
    def get_func_name(self, profil) -> list[SubButton]:
        # constrait : list = ["(", "args*", ")"]
        # pengumpul sementara 
        temp: str = None
        sub: SubButton = None
        single_tab: bool = True
        list_sub: list[SubButton] = []

        while len(profil) > 0:
            wahh = profil[len(profil)-1].get_name()
            
            # deteksi fungsi baru dalam token
            if wahh == "def":
                if sub :
                    sub.text_code(text=temp)
                    # print(temp)

                temp = ""
                # new sub button class
                temp += profil.pop().get_name()
                nama_fun = profil.pop().get_name()

                if nama_fun == "__init__":
                    continue
                
                btn_sub: SubButton = SubButton(nama_fun, "add_drive.png", hover_color="#f8a4a4")
                list_sub.append(btn_sub)
                temp += " " + nama_fun
                sub = btn_sub

                # masuk ke fungsi make interpreter
                # self.make_interpreter(profile=profil)
            
            elif wahh == "class":
                # masukan kedalam interpreter yang berjalan
                # buat interpreter baru
                return list_sub
            
            else :
                if temp :
                    res: str =  profil.pop().get_name()
                    if res == "NEW_LINE" :
                        temp+= "\n"
                        single_tab = True
                    elif res == "TAB":
                        if single_tab :
                            single_tab = False
                        else :
                            temp += "\t"
                            
                    elif res == ".":
                        temp += res
                    elif res == "(" :
                        temp +=  res
                    elif res == "/":
                        seek: str = profil[-1].get_name()
                        if seek == "/":
                            temp += res
                        else :
                            temp += res + " "
                    elif res == "*":
                        seek: str = profil[-1].get_name()
                        if seek == "*":
                            temp += res
                        else :
                            temp += res + " "

                    elif res == "=":
                        seek: str = profil[-1].get_name()
                        if seek == "=":
                            temp += res
                        else :
                            temp += res + " "

                    elif res == "-":
                        seek: str = profil[-1].get_name()
                        if seek == ">":
                            temp += res
                        else :
                            temp += res + " "
                    
                    elif res == '''"''':
                        seek: str = profil[-1].get_name()
                        if seek == '''"''':
                            temp += res
                        else :
                            temp += res + " "
                    else :
                        if len(profil) <= 0 :
                            temp += res
                            break

                        seek: str = profil[-1].get_name()

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
    
    def expression_helper(self, res: str, seek: str) -> bool:
        if res == "=":
            if seek == "=":
                return True
            else :
                return False

    def make_interpreter(self, profile) -> None:
        constrait: str = ["(", "kwargs", ")", ":"]
        register: str = ""

        # fungsi untuk mencari input
        while True:
            wahh, _, _, _ = profile[-1].get_token()
            if wahh == ")":
                profile.pop()
                break

            elif wahh == ":" :
                register = ""
                profile.pop()
                while True :
                    sets, _, _, _ = profile[-1].get_token()
                    if sets == ")" or sets == ",":
                        # dilakukan input ke button input
                        break

                    else :
                        register += sets
                        profile.pop()
            
            else :
                profile.pop()

        while True :
            wahh, _, _, _ = profile[-1].get_token()
            if wahh == "->" :
                print("output")
            
            elif wahh == ":":
                break

            else:
                profile.pop()
              
        return None