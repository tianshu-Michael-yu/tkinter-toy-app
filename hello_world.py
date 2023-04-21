import tkinter as tk

root = tk.Tk()
root.title("Hello World")

# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window open until the user closes it
root.mainloop()