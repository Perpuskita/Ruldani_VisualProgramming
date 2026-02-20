class Interpreter():

    def __init__(self, name, link, header, input_type, output_type ):
        self.name = name
        self.link = link
        self.header = []
        self.input = input_type
        self.output = output_type
    
    def atribute(self):
        return [["nama", self.name], ["link", self.link]]
    
    def folder_code(self, name, link):
        return f'''# baris untuk open folder \n{name} = '{link}'\n'''
    
    def code_saver(self, load):
        return self.folder_code(self.name.replace(" ", "_"), self.link), self.name.replace(" ", "_"), self.header
     
    def update_data(self, name, link):
        self.name = name
        self.link = link
    
