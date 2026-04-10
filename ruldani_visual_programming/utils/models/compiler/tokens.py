# peghubung dan pemisah antar token
class tokens():
    def __init__(self, name, begin: int = 1, end: int = 1, type_token: str = None):
        self.name   = name
        self.begin  = begin
        self.end    = end
        self.type = type_token
        self.priority = 1
    
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
