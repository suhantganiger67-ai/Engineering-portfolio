# write a function to check if a number is odd or even

import random


number = random.randint(1, 10)
print(number)  # Generate a random number between 1 and 10


def check_odd_even(number):
    if number % 2 == 0:
        print("Even")


check_odd_even(5)  # Example usage


# write a funtion to count the number of vowels in a string

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


count = count_vowels("Hello World")
print("Number of vowels:", count)  # Example usage


# write a function to pint a number is prime or not


def is_prime(number):
    if number <= 1:
        print(number, "is not a prime number.")
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(number, "is not a prime number.")


is_prime(7)  # Example usage


# write a return the average if a list of marks are parameters
