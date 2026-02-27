YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

class panic:
    def __init__(self):
        pass

    def node_not_match( self, e):
        print(f"node not match {e}")

    def bind_error(self, e):
        print(f"binding error {e}")

    def token_undev(self, e):
        print(f"{RED}token undefinition {e}")

panics = panic()