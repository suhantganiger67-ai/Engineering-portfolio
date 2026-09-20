import random

lucky_number = random.randint(1, 50+1)
guess = 0
lives = 5

while guess != lucky_number and lives > 0:
    guess = int(input("Guess a number between 1 and 50: "))

    if guess < lucky_number:
        print("Too low! Try again.")
    elif guess > lucky_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the lucky number:", lucky_number)
    lives -= 1
    if lives == 0:
        print("Game over! You've run out of lives.")
