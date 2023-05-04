import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Matplotlib in Tkinter App")
        self.root.geometry("800x600")
        self.tab_control = ttk.Notebook(self.root)

    def plot(self, master, x_data, y_data):
        fig = Figure(figsize=(6, 6))
        figure_canvas = FigureCanvasTkAgg(fig, master=master)
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ax = fig.add_subplot(111)
        ax.plot(x_data, y_data)

    def show(self):
        self.root.mainloop()

    def create_tab(self, tab_name = "tab"):
        tab = ttk.Frame(self.tab_control)
        self.tab_control.add(tab, text=tab_name)
        self.tab_control.pack(expand=1, fill='both')
        return tab

if __name__ == "__main__":
    app = App()
    tab2 = app.create_tab("tab2")
    app.plot(tab2, [1, 2, 3, 4, 5], [3, 5, 2, 6, 2]) 
    tab1 = app.create_tab("tab1") 
    app.plot(tab1, [1, 2, 3, 4, 5], [3, 5, 2, 6, 2])
    app.show()