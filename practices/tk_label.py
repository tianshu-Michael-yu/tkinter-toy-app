import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")
root.title('Label Widget Demo')

label = ttk.Label(root, text = "A Label with the Heletica font", font = ("Helvetica", 16))
label.pack(ipadx=10, ipady=10)

photo = tk.PhotoImage(file='~/Desktop/Screenshot 2023-04-13 at 7.51.44 AM.png')
image_label = ttk.Label(root, image=photo, text="A Label with an image", compound='top')
image_label.pack()

root.mainloop()