# function that counts to certain number

def count_to_ten():
    for i in range(0, 11):
        print(i)


count_to_ten()


# write a function that print even numbers

def even_num():
    for i in range(0, 11):
        if i % 2 == 0:
            print(i)


even_num()


# write a function to make multiplication table

def multiplication_table(num):
    for i in range(1, 11):
        table = num * i
        print(f'{num} x {i} = {table}')


multiplication_table(5)


# write a function check number is even or odd

def check_number():
    for i in range(0, 21):
        if i % 2 == 0:
            print(f'{i} is even')
        else:
            print(f'{i} is odd')


check_number()

# write a functions that prints number greater than 5
numbers = [2, 7, 4, 10, 3, 8, 1]


def greater_than_five():
    for num in numbers:
        if num > 5:
            print(num)


greater_than_five()


# write a function to count even numbers

numbers = [2, 5, 8, 11, 14, 17, 20]


def count_even_numbers():
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    print(f'The count of even numbers is: {count}')


count_even_numbers()


# greatest number in a list
numbers = [12, 45, 7, 89, 23, 56]


def greatest_number(numbers):
    greatest = 0
    for num in numbers:
        if num > greatest:
            greatest = num
    print(f'The greatest number is: {greatest}')


greatest_number(numbers)


# write a function that prints every string

def print_strings(strings):
    for char in "hello world":
        print(char)


print_strings("python")


# write a function to print specific string

def print_specific_string(word, target):
    count = 0
    for char in word:
        if char == target:
            count += 1
    print(f'The count of "{target}" in "{word}" is: {count}')


print_specific_string("hello world", "o")


# write function to count vowels in a string

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print(f'The count of vowels in "{string}" is: {count}')


count_vowels("hello world")


# functions to count uppercase letters in a string

def count_uppercase(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    print(f'The count of uppercase letters in "{string}" is: {count}')


count_uppercase("PyThOn Is FuN")
