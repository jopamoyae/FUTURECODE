from tkinter import *

window = Tk("Picture")
window.geometry("800x600")

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()


class Picture:
    def __init__(self, color_of_rectangle, color_of_polygon):
        self.color_of_rectangle = color_of_rectangle
        self.color_of_polygon = color_of_polygon

    def picture(self):
        canvas.create_rectangle(200, 200, 400, 400, fill=self.color_of_rectangle, outline='black')
        canvas.create_polygon(200, 200, 300, 150, 400, 200, fill=self.color_of_polygon, outline='black')

    def picture_2(self):
        canvas.create_rectangle(300, 300, 500, 400, fill=self.color_of_rectangle, outline='black')
        canvas.create_polygon(300, 300, 400, 250, 500, 300, fill=self.color_of_polygon, outline='black')


first_pic = Picture('pink', 'yellow')
first_pic.picture()
second_pic = Picture('orange', 'purple')
second_pic.picture_2()

window.mainloop()
