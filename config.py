from random import randint


class Weapon:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg


sword = Weapon('Sword', 5)


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.gold = 30
        self.char = randint(5, 20)
        self.pwr = randint(5, 20)
        self.wis = randint(5, 20)
    weapons = [sword]


def weapons_inv():
    for i in player.weapons:
        name = i.name
        return name


player = Player('')
