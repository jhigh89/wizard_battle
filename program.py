import creatures
import heroes
import random

def main():
    print_header()
    game_loop()

def print_header():
    print('-------------------')
    print('------Wizard-------')
    print('-------------------')
    print()

def game_loop():

    name = input('What is your name, brave adventurer? \n >>> ')
    print()
    hero_choices = random.choice(['Wizard', 'Knight', 'Rogue', 'Warrior'])
    
    if hero_choices == 'Wizard':
        hero = heroes.Wizard(name)
    elif hero_choices == 'Knight':
        hero = heroes.Knight(name)
    elif hero_choices == 'Rogue':
        hero = heroes.Rogue(name)
    else:
        hero = heroes.Warrior(name)

    print(f"You spawned in as a level {hero.level} {hero_choices} with {hero.hp} hp")
    print()

    while True:

        spawned_creature = creatures.random_creature_picker()

        print(f"As you strolled through the forest, a wild {spawned_creature.type} by the name of {spawned_creature.name} appeared in front of you.")
        print()
        print()
        cmd = input(f'Do you [a]ttack the {spawned_creature.type}, [r]un away, or [l]ook around for another creature? (Enter "x" to close the game.) \n >>> ').lower()
        if cmd == 'a':
            creature_defeated = False
            print()
            while creature_defeated == False:
                attack = hero.attack(hero.power,hero.crit_chance,hero.accuracy)
                print(f"You attack the {spawned_creature.type} and do {attack} damage.")
                spawned_creature.hp = spawned_creature.hp - attack
                if spawned_creature.hp <= 0:
                    print(f"You defeated the {spawned_creature.type} and gained {spawned_creature.xp} XP!")
                    print()
                    creature_defeated = True
                    hero.xp = hero.xp + spawned_creature.xp
        elif cmd == 'r':
            print('chose chicken')
        elif cmd == 'l':
            print('chose daydream')
        elif cmd == 'x':
            print('Chose real life. Cya around!')
            return False
        else:
            print('Huh? In all my years of adventuring, I\'ve never heard a command like that...')

if __name__ == '__main__':
    main()