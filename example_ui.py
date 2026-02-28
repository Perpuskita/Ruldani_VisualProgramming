from ruldani_visual_programming.utils.pages import button
import tkinter as tk
import customtkinter as ctk

if __name__ == "__main__":
    App:tk.Tk = tk.Tk()
    App.geometry("720x720")
    App.grid_rowconfigure(0,weight=1)
    App.grid_columnconfigure(0,weight=1)

    frame: ctk.CTkFrame = ctk.CTkFrame(master=App, height=200, width=300, fg_color="#363636")
    frame.grid(row=0, column=0, sticky = "n")
    frame.grid_propagate(False)
    btn:ctk.CTkButton = button(frame, image="logo.png")
    btn.grid(row=0, column=0)
    App.mainloop()
    