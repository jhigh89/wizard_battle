import random

# contains heroes available
class Hero:
    def __init__(self, name):
        self.name = name

    def attack(self,power,crit_chance,accuracy):
        '''
        The hero's attack method. Takes a power(int),crit_chance(int), and accuracy(int)
        variable to roll.
        '''
        attack = random.randint(1,power)
        crit = random.randint(1,100)
        attack_roll = random.randint(1,100)
        if attack_roll <= accuracy:
            if crit <= crit_chance:
                attack = attack * 2
                print("A critical hit!")
        else:
            attack = attack * .5
            print("A glancing blow...")
        return attack

    def defend(self,def_power,power,accuracy):
        '''
        The hero's defense method. Takes a def_power, power roll, and accuracy.
        If def power is equal to or greater than the creature's power,
        the attack is blocked!
        '''
        block = False
        difference = 0
        defense = def_power
        miss = False
        attack = random.randint(1,power)
        attack_chance = random.randint(1,100)
        if accuracy <= attack_chance:
            print('The creature missed his attack!')
            miss = True
            block = True
        if defense >= attack and miss == False:
            print('You successfully blocked the attack!')
            block = True
            miss = False
        if miss == False and block == False:
            difference = attack - defense
            print(f'Your defense failed, and the creature struck you for {difference} damage!')
        return block,difference,miss

class Knight(Hero):
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.power = 80
        self.def_power = 85
        self.crit_chance = 2
        self.accuracy = 80
        self.hp = random.randint(250,300)

class Wizard(Hero):
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.power = 40
        self.def_power = 30
        self.crit_chance = 4
        self.accuracy = 70
        self.hp = random.randint(50,100)

class Rogue(Hero):
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.power = 100
        self.def_power = 25
        self.crit_chance = 20
        self.accuracy = 95
        self.hp = random.randint(75,100)

class Warrior(Hero):
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.power = 100
        self.def_power = 25
        self.crit_chance = 10
        self.accuracy = 90
        self.hp = random.randint(150,200)