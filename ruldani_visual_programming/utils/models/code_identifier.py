from ruldani_visual_programming.utils.models.compiler import tokenizer
from ruldani_visual_programming.utils.models.code_database import interpreter
from ruldani_visual_programming.utils.models.button_config import Button, SubButton


class code_identifier:
    def __init__(self, rawtext: str)-> None:
        self.raw_text = rawtext
        self.conf_button = self.get_class_name()

    # mengambil nama class dari token yang diberikan
    def get_class_name(self) -> list[Button]:
        constrait : list = ["class", "id", "func", "id", "func", "func", "enter"]
        lexer = tokenizer(self.raw_text)
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

            nama, _, _, types = profil.pop().get_token()
            if types == "BUILT_IN_FUNCTION" and nama == "class":
                wahhid, _, _, _ = profil.pop().get_token()
                btn_now: Button = Button(wahhid, "home.png")

                # jump to get_func_name
                self.get_func_name(btn_now=btn_now, profil=profil)
                res.append(btn_now)

        return res
    
    # make sub_button
    def get_func_name(self, btn_now: Button, profil) -> None:
        # constrait : list = ["(", "args*", ")"]

        while len(profil) > 0:
            wahh, _, _, _ = profil[len(profil)-1].get_token()
            if wahh == "def":
                profil.pop()
                nama_fun,_, _, _ = profil.pop().get_token()

                if nama_fun == "__init__":
                    continue
                
                btn_sub: SubButton = SubButton(nama_fun, "add_drive.png", hover_color="#f8a4a4")
                btn_now.set_sub_buttons(btn_sub)

                # masuk ke fungsi make interpreter
                self.make_interpreter(profile=profil)
            
            elif wahh == "class":
                # masukan kedalam interpreter yang berjalan
                # buat interpreter baru
                return None
            
            else :
                profil.pop()

        return None
    
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