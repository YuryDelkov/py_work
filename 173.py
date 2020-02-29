from tkinter import *
from random import *

n = 50
mas = list(range(1, 4*n))

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

for i in range(0, 4*n-1):
    if mas[i] % 4 == 0:
        colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink', 
         'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
        x = mas[i]-mas[i+3]/2
        y = mas[i+1]-mas[i+2]/2
        canvas.create_rectangle(x, y, x + mas[i+3], y + mas[i+2], fill=colors)

root.mainloop()