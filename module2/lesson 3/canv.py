from tkinter import *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()

canvas.create_rectangle(200, 200, 400, 400, fill='pink')
canvas.create_polygon(200, 200, 300, 100, 400, 200, fill='orange', outline='black')
canvas.create_rectangle(220, 300, 270, 320, fill='white')

window.mainloop()
