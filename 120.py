from tkinter import *
 
root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

points = [30, 30, 80, 30, 10, 100, 30, 30] # Треугольник
canvas.create_polygon(points, fill='orange')

canvas.create_rectangle(80, 80, 170, 150, fill='red')

points = [100, 180, 150, 180, 170, 200, 150, 220, 100, 220, 80, 200, 100, 180] # Пятиугольник
canvas.create_polygon(points, fill='blue') 

points = [200, 180, 220, 200, 220, 220, 200, 240, 180, 220, 180, 200, 200, 180] # Шестиугольникs
canvas.create_polygon(points, fill='green')

root.mainloop()