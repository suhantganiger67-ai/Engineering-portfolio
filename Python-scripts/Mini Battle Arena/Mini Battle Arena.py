import random

fighters = ["Warrior","Mage", "Archer"]
fighters_HP = [20 , 15, 18]

print('Welcome to the Mini Battle Arena!⚔️')
players_choice = int(input('''Choose your fighter 
0 for Warrior
1 for Mage
2 for Archer
enter a number: '''))
if players_choice >= 3 or players_choice < 0:
    print("You typed an invalid number!")
elif players_choice == 0:
    print('''You chose Warrior!\n  ''')

elif players_choice == 1:
    print('''You chose Mage!🧙‍♂️\n  ''')

elif players_choice == 2:
    print('''You chose Archer!🏹\n  ''')

HP = fighters_HP[players_choice]
enemy_HP = 50
for rounds in range(1, 6):
    enemy_damage = random.choice([2 , 3, 4, 5])
    Your_damage = random.choice([10 , 15 , 20])
    HP -= enemy_damage
    enemy_HP -= Your_damage
    if rounds % 2 == 0:
        HP += 2
        print("You feel a surge of energy!")

    print(f"Round {rounds}")

    print(f"Enemy attacks!\n enemy damage: {enemy_damage}💥")
    print(f"You attack!\nYour damage: {Your_damage}💥")

    print(f"Your HP: {HP}💖")
    print(f"Enemy HP: {enemy_HP}💖")

    if HP <= 0:
        print("You have been defeated!💀")
        break
    elif enemy_HP <= 0:
        print("You have defeated the enemy!🏆")
        break