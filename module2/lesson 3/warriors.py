from random import randint


class Warrior:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, enemy):
        enemy.hp -= self.damage
        if enemy.hp > 0:
            print(f'"{self.name}" атаковал "{enemy.name}". {enemy.name} - {enemy.hp} единиц здоровья.')
        else:
            print(f'"{self.name}" атаковал "{enemy.name}". {enemy.name} убит.')
            enemy.hp = 0
        return enemy.hp


warrior1 = Warrior('Первый воин', 100, 20)
warrior2 = Warrior('Второй воин', 100, 20)
warriors = [warrior1, warrior2]

while True:
    attack_index = randint(0, 1)
    target_index = (attack_index + 1)%2
    target_hp = warriors[attack_index].attack(warriors[target_index])
    if target_hp == 0:
        print(f'{warriors[attack_index].name} победил!')
        break