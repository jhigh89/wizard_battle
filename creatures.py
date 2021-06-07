import random
from random_name import fantasy_name

# contains creature classes

class Dragon:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Dragon'
        self.level = random.randint(25,100)
        self.hp = self.level * 5
        self.xp = self.hp

class Rat:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Rat'
        self.level = random.randint(1,3)
        self.hp = self.level
        self.xp = self.level

class Bird:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Bird'
        self.level = random.randint(1,5)
        self.hp = self.level
        self.xp = self.level

class Orc:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Orc'
        self.level = random.randint(5,15)
        self.hp = self.level * 2
        self.xp = self.hp

class Troll:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Troll'
        self.level = random.randint(15,30)
        self.hp = self.level * 6
        self.xp = self.hp

class Polymorph:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Polymorph'
        self.level = 1
        self.hp = self.level
        self.xp = self.hp * 5

class Ghost:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Ghost'
        self.level = random.randint(15,35)
        self.hp = self.level * .5
        self.xp = self.level

class Demon:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Demon'
        self.level = random.randint(55,75)
        self.hp = self.level * 3
        self.xp = self.hp

class Giant:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Giant'
        self.level = random.randint(55,85)
        self.hp = self.level * 4.5
        self.xp = self.hp

class Cat:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Cat'
        self.level = random.randint(10,20)
        self.hp = self.level
        self.xp = self.hp

class Dog:
    def __init__(self):
        self.name = fantasy_name()
        self.type = 'Dog'
        self.level = random.randint(10,20)
        self.hp = self.level
        self.xp = self.hp

def random_creature_picker():
    '''
    Creates a random creature for the adventurer to encounter!
    '''
    creatures=['Dragon','Rat','Bird','Orc','Troll','Polymorph','Ghost','Demon','Giant','Cat','Dog']
    random_creature = random.choice(creatures)
    if random_creature == 'Dragon':
        creature = Dragon()
    elif random_creature == 'Rat':
        creature = Rat()
    elif random_creature == 'Bird':
        creature = Bird()
    elif random_creature == 'Orc':
        creature = Orc()
    elif random_creature == 'Troll':
        creature = Troll()
    elif random_creature == 'Polymorph':
        creature = Polymorph()
    elif random_creature == 'Ghost':
        creature = Ghost()
    elif random_creature == 'Demon':
        creature = Demon()
    elif random_creature == 'Giant':
        creature = Giant()
    elif random_creature == 'Cat':
        creature = Cat()
    else:
        creature = Dog()
    return creature