from random import randint


def appear(enemy, num):
    vowels = ('A', 'E', 'I', 'O', 'U')
    output = ''
    enemies = [enemy for i in range(0, num)]
    if len(enemies) > 1:
        if enemies[0].name[-1] == 's':
            print(f'{num} {enemy.name}es have appeared!')
        else:
            print(f'{num} {enemy.name}s have appeared!')
        return output
    elif len(enemies) == 1:
        enemies = [enemy]
        enemy_char = enemies[0].name[0]
        for vowel in vowels:
            if enemy_char == vowel:
                output = f'An {enemy.name} appeared!'
            else:
                output = f'A {enemy.name} appeared!'
        print(output)
        return enemies
    else:
        print("Maybe it's my imagination... There's no one to fight.")


def die(name, num):
    print(f"{name} #{num} has died.")


class FireEle:
    def __init__(self):
        self.name = "Fire Elemental"
        self.health = randint(15, 25)
        self.dmg = randint(5, 10)

    def attack(self):
        if randint(1, 3) == 1:
            print(f"{self.name} launches a fireball at you for {randint(5, 20)} fire damage!")
        else:
            print(f"{self.name} attacks you for {self.dmg}!")


class Bandit:
    def __init__(self):
        self.name = "Bandit"
        self.health = randint(6, 12)
        self.dmg = randint(2, 4)


class AeonNecrosis:
    def __init__(self):
        self.name = "Aeon Necrosis"
        self.health = randint(100, 150)
        self.dmg = randint(50, 75)
