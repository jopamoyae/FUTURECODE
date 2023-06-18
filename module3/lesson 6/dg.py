class Year:
    def __init__(self):
        self.days = 365
        self.season = 'summer'

    @property
    def days(self):
        return self.__days

    @days.setter
    def set_days(self, days):
        if days == 365 or days == 366:
            self.days = days
        else:
            raise Exception(f'Вы передали неккоректное значение, в году не может быть {days} дней.')


year = Year()
# print(year.get_days())
# year.set_days(364)
# print(year.get_days())