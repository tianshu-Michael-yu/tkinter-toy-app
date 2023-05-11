import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(root)
label.config(text="Hello, World!")
label.pack()

def button_clicked():
    label.config(text="Button clicked!")

button = ttk.Button(root)
button.config(text="Click me!", command=button_clicked)
button.pack()

def select(option):
    print(option)

ttk.Button(root, text="Option 1", command=lambda: select("Option 1")).pack()
ttk.Button(root, text="Option 2", command=lambda: select("Option 2")).pack()
ttk.Button(root, text="Option 3", command=lambda: select("Option 3")).pack()

root.mainloop()