import customtkinter as ctk
import tkinter as tk
from tkinter import colorchooser
import webcolors

class ColorPickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("CustomTkinter Color Picker")
        self.geometry("600x500")
        self.configure(fg_color="#2b2b2b")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Variables
        self.current_color = "#ff0000"
        self.hex_var = ctk.StringVar(value="#ff0000")
        self.rgb_var = ctk.StringVar(value="RGB(255, 0, 0)")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header = ctk.CTkLabel(self, text="Color Picker", 
                             font=ctk.CTkFont(size=24, weight="bold"))
        header.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        # Main frame
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Color display
        color_display = ctk.CTkFrame(main_frame, height=150, 
                                   fg_color=self.current_color,
                                   corner_radius=15)
        color_display.grid(row=0, column=0, padx=10, pady=20, sticky="ew")
        
        # Color information
        info_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        info_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        ctk.CTkLabel(info_frame, text="HEX:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=5, pady=5, sticky="w")
        
        hex_entry = ctk.CTkEntry(info_frame, textvariable=self.hex_var,
                               font=ctk.CTkFont(weight="bold"))
        hex_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        hex_entry.bind("<Return>", self.update_from_hex)
        
        ctk.CTkLabel(info_frame, text="RGB:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=5, pady=5, sticky="w")
        
        rgb_label = ctk.CTkLabel(info_frame, textvariable=self.rgb_var,
                               font=ctk.CTkFont(weight="bold"))
        rgb_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        info_frame.grid_columnconfigure(1, weight=1)
        
        # Sliders frame
        sliders_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        sliders_frame.grid(row=2, column=0, padx=10, pady=20, sticky="ew")
        
        # Red slider
        self.red_var = ctk.IntVar(value=255)
        red_slider = ctk.CTkSlider(sliders_frame, from_=0, to=255, 
                                 variable=self.red_var,
                                 progress_color="#ff0000", 
                                 button_color="#ff0000",
                                 command=self.update_from_sliders)
        red_slider.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkLabel(sliders_frame, text="R:", text_color="#ff0000").grid(
            row=0, column=0, padx=5, pady=5)
        
        # Green slider
        self.green_var = ctk.IntVar(value=0)
        green_slider = ctk.CTkSlider(sliders_frame, from_=0, to=255, 
                                   variable=self.green_var,
                                   progress_color="#00ff00", 
                                   button_color="#00ff00",
                                   command=self.update_from_sliders)
        green_slider.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkLabel(sliders_frame, text="G:", text_color="#00ff00").grid(
            row=1, column=0, padx=5, pady=5)
        
        # Blue slider
        self.blue_var = ctk.IntVar(value=0)
        blue_slider = ctk.CTkSlider(sliders_frame, from_=0, to=255, 
                                  variable=self.blue_var,
                                  progress_color="#0000ff", 
                                  button_color="#0000ff",
                                  command=self.update_from_sliders)
        blue_slider.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        ctk.CTkLabel(sliders_frame, text="B:", text_color="#0000ff").grid(
            row=2, column=0, padx=5, pady=5)
        
        sliders_frame.grid_columnconfigure(1, weight=1)
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        buttons_frame.grid(row=3, column=0, padx=10, pady=20, sticky="ew")
        
        # System color picker button
        system_btn = ctk.CTkButton(buttons_frame, text="System Color Picker",
                                 command=self.open_system_color_picker)
        system_btn.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        
        # Copy button
        copy_btn = ctk.CTkButton(buttons_frame, text="Copy HEX",
                               command=self.copy_hex)
        copy_btn.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        buttons_frame.grid_columnconfigure((0, 1), weight=1)
        
        # Set initial color
        self.update_color_display()
        
    def update_from_sliders(self, *args):
        r = self.red_var.get()
        g = self.green_var.get()
        b = self.blue_var.get()
        
        self.current_color = f"#{r:02x}{g:02x}{b:02x}"
        self.update_color_display()
        
    def update_from_hex(self, event=None):
        hex_value = self.hex_var.get().strip()
        
        # Validate hex format
        if not hex_value.startswith('#'):
            hex_value = '#' + hex_value
        
        if len(hex_value) == 7 and all(c in '0123456789abcdefABCDEF' for c in hex_value[1:]):
            try:
                # Convert hex to RGB
                r, g, b = webcolors.hex_to_rgb(hex_value)
                self.red_var.set(r)
                self.green_var.set(g)
                self.blue_var.set(b)
                self.current_color = hex_value
                self.update_color_display()
            except ValueError:
                # Reset to current color if invalid
                self.hex_var.set(self.current_color)
        else:
            # Reset to current color if invalid
            self.hex_var.set(self.current_color)
    
    def update_color_display(self):
        # Update all widgets that display the color
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkFrame) and hasattr(widget, 'winfo_children'):
                for child in widget.winfo_children():
                    if isinstance(child, ctk.CTkFrame) and child.winfo_height() == 150:
                        child.configure(fg_color=self.current_color)
        
        # Update text variables
        r, g, b = self.red_var.get(), self.green_var.get(), self.blue_var.get()
        self.hex_var.set(f"#{r:02x}{g:02x}{b:02x}")
        self.rgb_var.set(f"RGB({r}, {g}, {b})")
    
    def open_system_color_picker(self):
        color = colorchooser.askcolor(initialcolor=self.current_color,
                                    title="Choose a color")
        if color[0]:  # User didn't cancel
            r, g, b = [int(x) for x in color[0]]
            self.red_var.set(r)
            self.green_var.set(g)
            self.blue_var.set(b)
            self.current_color = color[1]
            self.update_color_display()
    
    def copy_hex(self):
        self.clipboard_clear()
        self.clipboard_append(self.hex_var.get())
        self.update()  # Required for clipboard to work

if __name__ == "__main__":
    # Set appearance mode and color theme
    ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"
    
    app = ColorPickerApp()
    app.mainloop()