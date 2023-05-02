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

    def plot(self, x_data, y_data):
        fig = Figure(figsize=(6, 6))
        ax = fig.add_subplot(111)
        ax.plot(x_data, y_data)
        figure_canvas = FigureCanvasTkAgg(fig, master=self.root)
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def show(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.plot([1, 2, 3, 4, 5], [3, 5, 2, 6, 2])
    app.show()