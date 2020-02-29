from tkinter import *
from datetime import datetime

root = Tk()
root.title('Электронные часы')
canvas = Canvas(root, width=570, height=170)
canvas.pack()

def number_clock(x, t):
    if (t > 1 or t == 0) and t != 4:
        points = [[x, 20], [x+5, 15], [x+55, 15], [x+60, 20], [x+50, 30], [x+10, 30]] # T
        canvas.create_polygon(points, outline='black', fill='cyan', width=1)
    if (t < 1 or t > 3) and t !=7:
        points = [[x, 23], [x+10, 33], [x+10, 73], [x, 83], [x-5, 78], [x-5, 28]] # TL
        canvas.create_polygon(points, outline='black', fill='cyan', width=1)
    if t != 5 and t != 6:
        points = [[x+60, 23], [x+50, 33], [x+50, 73], [x+60, 83], [x+65, 78], [x+65, 28]] # TR
        canvas.create_polygon(points, outline='black', fill='cyan', width=1) 
    if t != 0 and t != 1 and t != 7:
        points = [[x, 86], [x+10, 76], [x+50, 76], [x+60, 86], [x+50, 96], [x+10, 96]] # C
        canvas.create_polygon(points, outline='black', fill='cyan', width=1) 
    if t == 0 or t == 2 or t == 6 or t == 8:
        points = [[x, 89], [x+10, 99], [x+10, 139], [x, 149], [x-5, 144], [x-5, 94]] # BL
        canvas.create_polygon(points, outline='black', fill='cyan', width=1)
    if t != 2:
        points = [[x+60, 89], [x+50, 99], [x+50, 139], [x+60, 149], [x+65, 144], [x+65, 94]] # BR
        canvas.create_polygon(points, outline='black', fill='cyan', width=1)
    if t != 1 and t != 7 and t != 4:
        points = [[x, 152], [x+10, 142], [x+50, 142], [x+60, 152], [x+55, 157], [x+5, 157]] # B
        canvas.create_polygon(points, outline='black', fill='cyan', width=1)

while True:
    canvas.delete('all')
    time = str(datetime.now().time())
    x = 20
    for i in range(0, 8):
        if time[i] != ':':
            number_clock(x, int(time[i]))
            x += 80
        else: 
            canvas.create_rectangle(x, 50, x+15, 65, fill='cyan')
            canvas.create_rectangle(x, 110, x+15, 125, fill='cyan')
            x += 35    

    root.update()

