import customtkinter as ctk 

class styled_tooltip:
    def __init__(self, widget, text, **kwargs):
        self.widget = widget
        self.text = text
        self.tooltip = None
        
        # Custom styling
        self.bg_color = kwargs.get("bg_color", "#1a1a1a")
        self.text_color = kwargs.get("text_color", "#ffffff")
        self.font_size = kwargs.get("font_size", 11)
        self.offset_x = kwargs.get("offset_x", 15)
        self.offset_y = kwargs.get("offset_y", 5)
        
        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)
        
    def show(self, event=None):
        x = self.widget.winfo_rootx() + self.offset_x
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + self.offset_y
        
        self.tooltip = ctk.CTkToplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        self.tooltip.attributes("-topmost", True)
        self.tooltip.attributes("-alpha", 0.95)  # Transparansi
        
        label = ctk.CTkLabel(
            self.tooltip,
            text=self.text,
            fg_color=self.bg_color,
            text_color=self.text_color,
            corner_radius=8,
            padx=15,
            pady=8,
            font=ctk.CTkFont(size=self.font_size),
            justify="left"
        )
        label.pack()
        
    def hide(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
