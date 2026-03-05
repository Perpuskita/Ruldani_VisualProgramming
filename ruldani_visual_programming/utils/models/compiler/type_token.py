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
    "class", "import", "from", "as", "in", "#", "is"
]

OPERATOR = [
    "+", "-", "*", "/", "//", "%", "**",
    "==", "!=", ">", "<", ">=", "<=","="
]


class type_token:
    def __init__(self, name, content ,binding_power):
        self.name = name
        self.binding_power = binding_power

    def cek_content(token_cek:str ):
        return None
    
    def get_bindingpower(self):
        return self.binding_power