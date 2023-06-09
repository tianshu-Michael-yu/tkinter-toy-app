import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np 

matplotlib.use('TkAgg')

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Matplotlib in Tkinter App")
        self.root.geometry("800x600")

    def plot(self, x_data, y_data):
        fig = self.create_figure()
        ax = fig.add_subplot(111)
        ax.plot(x_data, y_data)

    def animate(self):
        fig = self.create_figure()
        ax = fig.add_subplot(xlim=(0, 4), ylim=(-2, 2))
        line, = ax.plot([], [], 'bo',lw=3)
        sin = Sine(line)
        self.start_animation(fig, sin.init, sin.animate)

    def start_animation(self, fig, init, animate):
        anim = FuncAnimation(fig, animate, init_func=init,
                                    frames=200, interval=20, blit=True)
        self.figure_canvas.draw()

    def create_figure(self):
        fig = Figure(figsize=(6, 6))
        figure_canvas = FigureCanvasTkAgg(fig, master=self.root)
        tk_widget = figure_canvas.get_tk_widget()
        tk_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.figure_canvas = figure_canvas
        return fig

    def show(self):
        self.root.mainloop()

class Sine:
    def __init__(self, line: matplotlib.lines.Line2D) -> None:
        self.line = line
    
    def animate(self, i):
        x = np.linspace(0, 4, 100)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        self.line.set_data(x, y)
        return self.line,

    def init(self):
        self.line.set_data([], [])
        return self.line,

if __name__ == "__main__":
    app = App()
    app.animate()
    app.show()