# menetapkan predikat untuk renderer 
# digunakan pada future proof
# #dict
# #input
# #output

class code_server_io:
    def __init__(self, nama_var: str, tipe_token: str):
        self.nama_var = nama_var
        self.tipe_token = tipe_token
        pass

    def reverse_dictionary(self) -> str :
        return

class code_server_pref(code_server_io) :
    def __init__(self, nama_variabel: str, tipe_token: str, value):
        super.__init__(nama_var = nama_variabel, tipe_token = tipe_token)
        self.value = value
        pass

    def reverse_dictionary(self) -> str :
        return f"{self.nama_variabel}"


DICT = "#dictxx%"
INPUT = "#inputxx%"
OUTPUT = "#outputxx%"

class code_server:
    def __init__(self):
        self.input: list = []
        self.pref: dict = {}
        self.output: list = []
        self.code: list = []

    def make_input(self, token: str):
        self.input.append(token)
        self.make_code(token=token)
        return None
    
    def make_pref(self, token: str, value) -> None:
        self.pref[token] = value
        self.make_code(DICT)
        self.make_code(token=token)
        return None
    
    def make_output(self, token: str) -> None:
        self.output.append(token)
        self.make_code(token=token)
        return None
    
    def make_code(self, token: str) -> None:
        self.code.append(token)
        return None

    def get_pref(self, name: str):
        return self.pref[name]
    
    def reverse_code(self)-> None:

        print(f"input {self.input}")
        print(f"output {self.output}")
        print(self.pref)

        return None