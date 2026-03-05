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


class lexical_analysis ():
    def __init__(self, token=None):
        self.token = token
        pass
    
    def detection(self, char, DEF):
        for separate in DEF:
            if char == separate:
                return separate
        return False
    
    def type_lexer(self, char:str) -> str:

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
        
        return "ID"

if __name__ == "__main__":
    lexer = lexical_analysis()
    print(lexer.type_lexer("oio"))