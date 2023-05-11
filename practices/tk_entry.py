import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Sign In")

email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    """This function is called when the login button is clicked""" 
    msg = f"You entered email: {email.get()} and password: {password.get()}"
    showinfo(title="Information", message=msg)

sigin_frame = ttk.Frame(root)
sigin_frame.pack(padx=10, pady=10, fill = 'x', expand = True)

email_label = ttk.Label(sigin_frame, text="Email:")
email_label.pack(fill='x', expand=True)
email_entry = ttk.Entry(sigin_frame, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

password_label = ttk.Label(sigin_frame, text="Password:")
password_label.pack(fill='x', expand=True)
password_entry = ttk.Entry(sigin_frame, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

login_button = ttk.Button(sigin_frame, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady = 10)

root.mainloop()