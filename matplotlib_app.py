import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matplotlib in Tkinter App")
        self.geometry("800x600")
        self.create_tab()

    def create_figure(self, master):
        fig = Figure(figsize=(6, 6))
        figure_canvas = FigureCanvasTkAgg(fig, master=master)
        ax = fig.add_subplot(111)
        x = [1, 2, 3, 4, 5]
        y = [3, 5, 2, 6, 2]
        ax.plot(x, y)
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    def create_tab(self):
        tab_control = ttk.Notebook(self)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text="Tab 1")
        tab_control.add(tab2, text="Tab 2")
        tab_control.pack(expand=1, fill='both')
        self.create_figure(tab1)
        self.create_figure(tab2)

if __name__ == "__main__":
    app = App()
    app.mainloop()