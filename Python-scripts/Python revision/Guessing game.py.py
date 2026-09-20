import random

lucky_number = random.randint(1, 100)
guess = 0

while guess != lucky_number:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < lucky_number:
        print("Too low! Try again.")
    elif guess > lucky_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the lucky number:", lucky_number)
