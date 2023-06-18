from tkinter import *
import random

window = Tk()
window.geometry('600x600')
window.title('Алхимик')


class Waves:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    image = PhotoImage(
        file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\2979114.png").subsample(6, 6)

    def __add__(self, other):
        pass


class Jug:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    image = PhotoImage(file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\free-icon-pottery-7942410.png").subsample(4, 4)

    def __add__(self, other):
        pass


class Steam:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    image = PhotoImage(file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\aroma.png").subsample(4, 4)

    def __add__(self, other):
        pass


class Clay:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    image = PhotoImage(file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\1230733.png").subsample(4, 4)


class Dust:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    image = PhotoImage(file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\free-icon-dust-2396941.png").subsample(4, 4)


class Wind:
    image = PhotoImage(file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\wind.png").subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Waves()


class Earth:
    image = PhotoImage(file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\ground.png").subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Water):
            return Clay()


class Fire:
    image = PhotoImage(file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\free-icon-fire-9509865.png").subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Clay):
            return Jug()


class Water:
    image = PhotoImage(file=r"C:\Users\2\PycharmProjects\FUTURECODE\module3\lesson 7\free-icon-water-drop-4246703.png").subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Clay()
        elif isinstance(other, Wind):
            return Waves()


canvas = Canvas(width=600, height=600)
canvas.pack()

elements = [Earth(), Water(), Wind(), Fire()]
for elem in elements:
    canvas.create_image(random.randint(50, 500), random.randint(50, 500), image=elem.image)


def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_ids) == 2:
        image_id_1, image_id_2 = images_ids[0], images_ids[1]

        elem1 = elements[image_id_1 - 1]
        elem2 = elements[image_id_2 - 1]

        new_elem = elem1 + elem2
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)

    canvas.coords(images_ids, event.x, event.y)


window.bind('<B1-Motion>', move)

window.mainloop()
