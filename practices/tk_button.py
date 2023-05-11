import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("400x300")
root.resizable(False, False)
root.title("Button Widget Demo")

exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(padx=10, pady=10)

def download():
    showinfo(title="Download", message="Downloading...")

button_icon = tk.PhotoImage(file="~/Downloads/download_button.png")

download_button = ttk.Button(root, image = button_icon, text="Download", compound = 'left', command=download)
download_button.pack(padx=10, pady=10)

root.mainloop()