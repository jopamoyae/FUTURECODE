class Human:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.__date_of_birth = date_of_birth

    def __info(self):
        print(self.name, self.__date_of_birth)


human = Human('Elvira', '04/08/2006')
print(human._Human__date_of_birth)
human._Human__date_of_birth = '01/01/2023'
print(human._Human__date_of_birth)

