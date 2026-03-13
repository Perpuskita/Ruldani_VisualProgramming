class interpreter():
    def __init__(self, name, input_type, output_type, link = None ):
        self.name = name
        self.link = link
        self.framework = []
        self.selected_framework: str = ""
        self.header: list = []
        self.selected_header: str = ""
        self.input = input_type
        self.output = output_type
        self.code_server: list[str] = []

    def set_code_server(self, loader: list[str]):
        return None

    def set_framework(self, framework: str)->None:
        if len(framework) == 0 :
            self.selected_framework = framework
        self.framework.append(framework)
        return None
    
    def set_header(self, header: str) -> None:
        if len(header) == 0 :
            self.selected_framework = header

        self.header.append(header)
        return None

    def atribute(self) -> list[str]:
        result: list[str] = ["nama", self.name]
        if self.link is not None :
            result.append(["link", self.link])

        return result
    
    def folder_code(self, name, link):
        return f'''# baris untuk open folder \n{name} = '{link}'\n'''
    
    def code_server(self, load):
        return self.folder_code(self.name.replace(" ", "_"), self.link), self.name.replace(" ", "_"), self.header
     
    def update_data(self, name, link):
        self.name = name
        self.link = link
    
