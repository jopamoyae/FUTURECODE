class Pet:
    def __init__(self, has_tail, legs, name, ears):
        self.has_tail = has_tail
        self.legs = legs
        self.name = name
        self.ears = ears

    def __str__(self):
        return f'У {self.name} {self.legs} ноги и {"есть хвост" if self.has_tail else "хвоста нет"}. ' \
               f'У него {"есть ушки" if self.ears else "нет ушек"}.'

    def sound(self):
        pass


class Dog(Pet):
    def __init__(self, legs, name, ears):
        super().__init__(name=name, legs=legs, ears=ears, has_tail=True)


dog = Dog(4, 'Буба', True)

print(dog)



# pet1 = Pet(has_tail=True, legs=4, name='', ears=True)
# pet2 = Pet(has_tail=True, legs=4, name='', ears=True)
# pet3 = Pet(has_tail=True, legs=4, name='', ears=True)
