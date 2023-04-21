import tkinter as tk

def find_center_coordinate(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    center_x = int((screen_width / 2) - (width / 2))
    center_y = int((screen_height / 2) - (height / 2))

    return center_x, center_y

root = tk.Tk()
root.title("Tkinter Window Demo")
width = 400
height = 300
center_x, center_y = find_center_coordinate(root, width, height)
root.geometry(f"{width}x{height}+{center_x}+{center_y}")

root.mainloop()