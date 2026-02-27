from PIL import Image
import os
import customtkinter as ctk

class image:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        pass
    
    def get_image(self, filename: str, dimension: list[int]) -> ctk.CTkImage:
        icon_path = os.path.join(self.base_dir, "icons", filename)
        icon = ctk.CTkImage(Image.open(icon_path), size=(dimension[0], dimension[1]))
        return icon


if __name__ == "__main__":
    img = image()
    hasil = img.get_image("logo.png", [25, 25])
    print(hasil)
