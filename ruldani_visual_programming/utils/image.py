from PIL import Image
import os
import customtkinter as ctk

class image(ctk.CTkImage):
    def __init__(self, filename: str, dimension: list[int]):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "icons", filename)
        image_pil = Image.open(icon_path)
        super().__init__(light_image=image_pil, dark_image=image_pil, size=(dimension[0], dimension[1]))

if __name__ == "__main__":
    img = image("logo.png", [20,20])
    print(img)
