from ruldani_visual_programming.utils.pages import pages
from ruldani_visual_programming.utils.models import models

class presenters:
    def __init__(self, view: pages, model: models):
        self.view: pages = view
        self.model: models = model

    def initial_button(self) -> list:
        buttons: list = [
            "neural network", "convolutional NN"
        ]
        return buttons
    
    def initial_subbutton(self) -> list:
        sub_buttons = [["undo.png", "cpm2.png", "cpm1.png", "cpm3.png" ], [ "cpm2.png", "undo.png", "undo.png"]]
        return sub_buttons

    def get_frame_icon(self):
        return None
    
