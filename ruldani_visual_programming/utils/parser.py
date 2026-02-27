from tokenizer import token
import error


# Nanti kuubah jadi immutable maps
# Pengenalan lingkungan fungsi
BUILT_IN_FUNCTION = ["BUILT_IN_FUNCTION", 3.0]
FUNC = ["FUNC", 1.1]
SEPARATOR = ["SEPARATOR", 2.0 ]
NEW_LINE = ["NEW_LINE", 3.0]

# Pengenalan lingkungan ID
ID = ["ID", 1.0]

# Container
BINDING_POWER = [BUILT_IN_FUNCTION, FUNC, SEPARATOR, ID, NEW_LINE]


class pratt_ast:
    def __init__(self, token_ast : token):
        self.token = token
        self.right = None
        self.left = None

    def right_join(self):
        return
    
    def left_join(self):
        return

class parser:
    def __init__(self, tokens : list ):
        self.tokens = tokens
        # penambahan token eof untuk pengenalan token end
        self.tokens.append(token("eof"))
        self.make_ast()
    
    def make_ast(self)-> pratt_ast:
        # variable for indicator
        Op_temp: pratt_ast
        len_token = len(tokens)-1

        # token looper
        for i in range(0, len_token):

            # binding power tebesar
            most = self.op_binding_power(i=i, len_token=len_token)

        return Op_temp

    def op_binding_power(self, i, len_token ) -> int:
        seek = self.seek_token(i)
        token_i = self.consume_token(i).type
        bind_i = self.binding_power(token_i)

        # Deklarasi binding power terbesar
        binding_power = most

        # Cari binding power terbesar
        for j in range (i, len_token):
            token_j = self.seek_token(j).type
            bind_j = self.binding_power(token_j)

            # Jika binding power terbesar maka ubah binding power
            if bind_j > most:
                most = bind_j
                binding_power = j
        
        return binding_power

    def add_ast(root: token, left:token, right:token):

        return None
                            
    def binding_power(self, token_types:str) -> float:
        for types in BINDING_POWER:
            if token_types == types[0]:
                return types[1]
        
        return error.panic.token_undev(token_types)
            

    def seek_token(self, i:int)-> token:
        return tokens[i+1]

    def consume_token(self, i:int)-> token:
        return tokens[i]

# testing

if __name__ == "__main__":
    from tokenizer import tokenizer
    
    daest = """class ast:
    def __init__(name):
        pass """

    tokens = tokenizer(daest).token

    # for i, tokenn in enumerate(tokens):
    #     print(tokenn.type)

    parser_n = parser(tokens=tokens)

    
    