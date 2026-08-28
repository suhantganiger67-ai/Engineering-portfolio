print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.🤑💎")
print("Your mission is to find the treasure.")
choice1 = input('You arrive at a mysterious crossroad.\n'
                'Where do you want to go? Type "left" or "right":')

if choice1 == "left" or choice1 == "Left" or choice1 == "LEFT":
    choice2 = input('You reach a lake🌊.\n'
                     'Do you want to "swim"🏊 across or "wait" for a boat?⛵')
    if choice2 == "boat" or choice2 == "Boat" or choice2 == "BOAT":
        choice3 = input('A boat⛵ arrives and takes you to a mysterious island🏝️.\n'
                        'You see three doors: Red, Blue, and Yellow.\n'
                        'Which door do you choose?')
        if choice3 == "red" or choice3 == "Red" or choice3 == "RED":
            print('🔥 You were burned by fire!'
                  'Game Over!')
        elif choice3 == "blue" or choice3 == "Blue" or choice3 == "BLUE":
            print('🐻 You were eaten by beasts!'
                  'Game Over!')
        elif choice3 == "yellow" or choice3 == "Yellow" or choice3 == "YELLOW":
            print("YAYYYY!!, You found the TREASURE")
        else:
            print("🚪 That isn't a valid door.\n"
                  "Game Over!")

    else:
        print('🐟 You were attacked by a trout!'
              'Game Over!')
else:
    print("GAME OVER!!, you fell into a hole!!")
