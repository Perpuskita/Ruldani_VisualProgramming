from ruldani_visual_programming.utils import highlight

TEXT_COLOR = "#ffffff"
DARK_COLOR = "#000000"

if __name__ == "__main__":
    
    import tkinter as tk
    import os

    def read_file_to_string(file_path):
        """Membaca file text menjadi string dengan error handling"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        try:
            with open(f"{base_dir}{file_path}", 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' tidak ditemukan")
            return None
        except Exception as e:
            print(f"Error membaca file: {e}")
            return None

    root = tk.Tk()
    root.geometry("1080x720")
    root.configure(bg=DARK_COLOR)

    root.title("ayo semangat ngodingnya biar dpet istri cantik")

    # Membuat Textbox
    textbox = tk.Text(
        root, 
        width=0, 
        height=20, 
        bg=DARK_COLOR,
        fg= TEXT_COLOR,
        bd=0, 
        font=("Consolas", 12), 
        tabs=("1c")
    )
    textbox.pack(expand=True, fill="both")

    text = read_file_to_string("/ruldani_visual_programming/utils/button.py")
    # configure 
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("end", text)

    # loop pada tokenizer
    high = highlight(textbox)

    root.mainloop()