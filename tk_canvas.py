import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Rectangle')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER,padx=10, pady=10, expand=True, fill=tk.BOTH)

canvas.create_rectangle((100, 100), (300, 300), fill='green')
points = (
    (200, 150),
    (500, 350),
)
canvas.create_oval(*points, fill='purple')
# create a polygon
points = (
    (100, 300),
    (200, 200),
    (300, 300),
)
canvas.create_text(
    (300, 100),
    text="Canvas Demo",
    fill="orange",
    font='tkDefaeultFont 24'
)

rectangle_item = canvas.create_polygon(*points, fill='blue')
canvas.tag_bind(rectangle_item, '<Button-1>', lambda x: canvas.delete(rectangle_item))

root.mainloop()