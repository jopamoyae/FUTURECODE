class User:
    def __init__(self, name, hp, attack_method, damage):
        self.name = name
        self.hp = hp
        self.attack_method = attack_method
        self.damage = damage

    def __str__(self):
        return f'{self.name} имеет {self.hp} здоровья. Его оружие: {self.attack_method}, наносящее {self.damage} урона.'


class Warrior(User):
    pass


print(Warrior('Воин', 100, 'меч', 20))


class Wizard(User):
    pass


print(Wizard('Маг', 200, 'посох', 25))


class Archer(User):
    pass


print(Archer('Лучник', 150, 'лук', 20))
# warrior = Warrior(100, 'sword', 20)
# wizard = Wizard(200, 'stick', 50)
# archer = Archer(100, 'bow', 25)



