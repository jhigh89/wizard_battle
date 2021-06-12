import creatures
import heroes
import random

def main():
    print_header()
    game_loop()

def print_header():
    print('\n-/-\-/-\--/-\-/-\--/-\-/-\--/-\-/-\--/-\-/-\-')
    print('-/-\-/-\------Roguelike RPG Lite-----/-\-/-\-')
    print('-/-\-/-\--/-\-/-\--/-\-/-\--/-\-/-\--/-\-/-\-')
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

    print(f"You spawned in as a level {hero.level} {hero_choices} with {hero.hp} hp.")
    print()

    creatures_defeated = 0
    died = False
    quit_game = False

    while quit_game == False and died == False:
        
        spawned_creature = creatures.random_creature_picker()
        if spawned_creature.type == "Polymorph":
            spawned_creature.level == hero.level

        print(f"As you walk through the dungeon, a wild {spawned_creature.type} by the name of {spawned_creature.name} appears in front of you.")
        print()
        print()
        cmd = input(f'Do you [f]ight the {spawned_creature.type} or [l]ook around for another creature? (Enter "x" to close the game.) \n >>> ').lower()
        if cmd == 'f':
            battle_finished = False
            print()
            print('-/-\-/-\--/-\-/-\--/-\-/-\--/-\-/-\--/-\-/-\-')
            print('------------------F-I-G-H-T------------------')
            print('-\-/-\-/--\-/-\-/--\-/-\-/--\-/-\-/--\-/-\-/-\n')
            while battle_finished == False:
                battle_menu = input("[A]ttack \n[D]efend \n[S]pecial \n[R]un \n\n >>>").lower()
                if battle_menu == 'a': 
                    print()
                    attack = hero.attack(hero.power,hero.crit_chance,hero.accuracy)
                    defend = spawned_creature.defend(spawned_creature.def_power,attack)
                    if defend != True:
                        print(f"You attack the {spawned_creature.type} and do {attack} damage.")
                        spawned_creature.hp = spawned_creature.hp - attack
                    else:
                        print(f"{spawned_creature.name} seems unphased by your attack!")
                    if spawned_creature.hp <= 0:
                        print(f"You defeated the {spawned_creature.type} and gained {spawned_creature.xp} XP!\n")
                        print()
                        hero.xp = hero.xp + spawned_creature.xp
                        creatures_defeated += 1
                        battle_finished = True
                    else:
                        print(f"The creature has {spawned_creature.hp} hp left.")
                    continue
                if battle_menu == 'd':
                    hero_defend = hero.defend(hero.def_power,spawned_creature.power,spawned_creature.accuracy)
                    print(hero_defend)
                    hero.hp = hero.hp - hero_defend[1]
                    if hero.hp <= 0:
                        print(f'You died. We will forever honor your bravery! You defeated {creatures_defeated} creatures this run.')
                        died = True
                        battle_finished = True
                    continue
                if battle_menu == 's':
                    print('You can achieve anything you set your mind to. :)\n')
                    continue
                if battle_menu == 'r':
                    print('You chose to run. Probably a good idea!\n')
                    battle_finished = True
                else:
                    print('\nYou momentarily forget what you are doing as you chose an option outside of your battle options!')

        elif cmd == 'l':
            print('You avoid the gaze of the creature and turn down another hallway.')
        elif cmd == 'x':
            quit_game = True
            print(f'You defeated {creatures_defeated} creatures on this run!')
            print('Chose real life. Cya around!')
            return quit_game
        else:
            print('Huh? In all my years of adventuring, I\'ve never heard a command like that...')

if __name__ == '__main__':
    main()