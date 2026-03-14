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
                jump += self.get_func_name(btn_now=btn_now, profil=profil)
                res.append(btn_now)

        return res
    
    # make sub_button
    def get_func_name(self, btn_now: Button, profil) -> int:
        # constrait : list = ["(", "args*", ")"]
        jump = 1

        while len(profil) > 0:
            wahh, _, _, _ = profil.pop().get_token()
            
            if wahh == "def":
                nama_fun,_, _, _ = profil.pop().get_token()
                
                if nama_fun == "__init__":
                    continue
                
                btn_sub: SubButton = SubButton(nama_fun, "add_drive.png", hover_color="#f8a4a4")
                btn_now.set_sub_buttons(btn_sub)

                # masuk ke fungsi make interpreter
                # jump += self.make_interpreter(profile=profil, sub_button=btn_sub, nama = nama_fun)
                jump += 1
            
            elif wahh == "class":
                # masukan kedalam interpreter yang berjalan
                # buat interpreter baru
                return jump
        return jump
    
    def make_interpreter(self, profile, sub_button: SubButton, nama: str) -> int:
        constrait: str = ["(", "kwargs", ")", ":"]
        jump = 1
        inputs: list = []
        output: list = []
        intr: interpreter = interpreter()
        register: str = ""

        for k in reversed(range(len(profile))):
            wahh, _, _, _ = profile.pop().get_token()
            if wahh == ":" :
                wahhw: str = profile.pop().get_token()

                while wahhw != ",":
                    register += wahhw

                register=""

            elif wahh == ")":
                break

            else:
                if register != "":
                    print(wahh)
            
        for k in reversed(range(len(profile))):
            wahh, _, _, _ = profile[k].get_token()
            if wahh == ":" :
                break

            elif wahh == "->":
                wahhw, _, _, _ = profile[k-1].get_token()            
        
        return jump