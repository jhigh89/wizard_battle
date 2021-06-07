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

    while True:

        spawned_creature = creatures.random_creature_picker()

        print(f"As you strolled through the forest, a wild {spawned_creature.type} by the name of {spawned_creature.name} appeared.")

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? (Enter "x" to close the game.) \n >>> ').lower()
        if cmd == 'a':
            print('chose violence')
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