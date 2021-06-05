import random

class Knight:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.hp = random.randint(250,300)

class Wizard:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.hp = random.randint(50,100)

class Rogue:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.hp = random.randint(75,100)

class Warrior:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.hp = random.randint(150,200)