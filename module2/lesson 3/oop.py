from tkinter import *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()


class House:
    def __init__(self, square, count_of_floors, color, color_of_triangle):
        self.square = square
        self.count_of_floors = count_of_floors
        self.color = color
        self.color_of_triangle = color_of_triangle

    def __str__(self):
        return f'Дом площадью: {self.square}, количество этажей: {self.count_of_floors}, цвет дома: {self.color}.'

    def print_info(self):
        print(f'Дом площадью: {self.square}, количество этажей: {self.count_of_floors}, цвет дома: {self.color}.')

    def do_something(self):
        pass

    def build_house(self):
        canvas.create_rectangle(200, 200, 400, 400, fill=self.color, outline='red')
        canvas.create_polygon(200, 200, 300, 150, 400, 200, fill=self.color_of_triangle)


house = House(200, 10, 'red', 'orange')
house.build_house()
house2 = House(300, 15, 'green', 'blue')
house2.build_house()
# print(house.square)
# print(house.count_of_floors)
# print(house.color)


# class House2:
#     square = 400
#     count_of_floors = 30
#     color = 'red'


# class Auto:
#     def __init__(self, brand, max_speed, weight):
#         self.brand = brand
#         self.max_speed = max_speed
#         self.weight = weight
#
# my_favorite_auto = Auto('BMW', 400, 3)
# andrey_favorite_auto = Auto('Mercedes', 500, 2)
#
# print(my_favorite_auto.brand)
# print(andrey_favorite_auto.brand)

window.mainloop()