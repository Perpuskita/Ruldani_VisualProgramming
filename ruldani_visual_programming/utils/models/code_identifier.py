from ruldani_visual_programming.utils.models.compiler import tokenizer
from ruldani_visual_programming.utils.models.code_database import interpreter
from ruldani_visual_programming.utils.models.button_config import Button, SubButton


class code_identifier:
    def __init__(self, rawtext: str)-> None:
        self.lexer = tokenizer(rawtext)
        self.conf_button = self.get_class_name()

    def get_class_name(self) -> list[Button]:
        constrait : list = ["class", "id", "func", "id", "func", "func", "enter"]
        profil = self.lexer.token
        res: list[Button] = []

        jump: int = 0
        for i in range(len(profil)) :
            if jump != 0 :
                jump -= 1
                continue

            nama, _, _, types = profil[i].get_token()
            if types == "BUILT_IN_FUNCTION":
                if nama == "class":
                    wahhid, _, _, _ = profil[i+1].get_token()
                    btn_now: Button = Button(wahhid, "home.png")

                    for j in range(len(profil) - i-1):
                        now: int = j+i + 1
                        wahh, _, _, _ = profil[now].get_token()
                        if wahh == "def":
                            nama_fun,_, _, _ = profil[now+1].get_token()
                            if nama_fun == "__init__":
                                continue

                            btn_sub: SubButton = SubButton(nama_fun, "add_drive.png", hover_color="#f8a4a4")
                            btn_now.set_sub_buttons(btn_sub)

                        elif wahh == "class":
                            jump -= 1
                            break
                        jump += 1
                    jump += 1
                    res.append(btn_now)
        return res
    
    def get_func_name(self, next : int) -> None:
        constrait : list = ["class", "id", "func", "id", "func", "id", "id", "func", "enter"]

        return None
    
    def configuration(self) -> None:
        new: interpreter = interpreter(name="test", input_type="test", output_type="test")
        new.set_framework("yess")
        new.set_header("ohh no")

        return None