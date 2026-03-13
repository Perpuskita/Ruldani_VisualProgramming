from ruldani_visual_programming.utils.pages import pages
from ruldani_visual_programming.utils.models import models

class presenters:
    def __init__(self, view: pages, model: models):
        self.view: pages = view
        self.model: models = model

    def initial_button(self) -> list:
        return self.model.get_button()
    
    def initial_subbutton(self) -> list:
        return self.model.get_sub_button()
    
    def make_visual_programming(self):
        print("presenter : membuat node baru")
        return None

    def assign(self, button, subbutton):
        return None
    
    def get_higlight(self, text):
        return None

    def get_frame_icon(self):
        return None
    
