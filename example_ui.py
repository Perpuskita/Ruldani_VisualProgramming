# from ruldani_visual_programming.utils.pages.atomic import button, logo
# import tkinter as tk
# import customtkinter as ctk

# if __name__ == "__main__":
#     App:tk.Tk = tk.Tk()
#     App.geometry("300x200")
#     App.grid_rowconfigure(0,weight=1)
#     App.grid_columnconfigure(0,weight=1)

#     frame: ctk.CTkFrame = ctk.CTkFrame(master=App, height=200, width=300, fg_color="#363636")
#     frame.grid(row=0, column=0, sticky = "n")
#     frame.grid_propagate(False)
#     # btn:ctk.CTkButton = button(frame, icon="logo.png")
#     # btn.grid(row=0, column=0)
#     logo_img = logo(master=frame, logo_image="logo.png")
#     logo_img.grid(row=0, column=0)
#     App.mainloop()

import customtkinter as ctk

def bezier_points(x1, y1, cx1, cy1, cx2, cy2, x2, y2, num_points=100):
    points = []
    for t in range(num_points + 1):
        t /= num_points
        x = (1 - t) ** 3 * x1 + 3 * (1 - t) ** 2 * t * cx1 + 3 * (1 - t) * t ** 2 * cx2 + t ** 3 * x2
        y = (1 - t) ** 3 * y1 + 3 * (1 - t) ** 2 * t * cy1 + 3 * (1 - t) * t ** 2 * cy2 + t ** 3 * y2
        points.append((x, y))
    return points

def update_curve(canvas, x1, y1, x2, y2):
    # Update the coordinates for the curve
    cx1, cy1 = (x1 + x2) / 2, y1
    cx2, cy2 = (x1 + x2) / 2, y2
    points = bezier_points(x1, y1, cx1, cy1, cx2, cy2, x2, y2)
    canvas.create_line(points, fill="blue", width=2, tags="line", smooth=True)


app = ctk.CTk()
app.geometry("400x300")

canvas = ctk.CTkCanvas(app, width=400, height=300, bg="white")
canvas.pack()

# Horizontal line
canvas.create_line(50, 100, 350, 100, fill="gray", width=2)

# Vertical line
canvas.create_line(200, 50, 200, 250, fill="gray", width=2)

# Diagonal line
update_curve(canvas, 50, 50, 350, 250)

app.mainloop()