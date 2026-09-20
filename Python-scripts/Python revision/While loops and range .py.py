# # practice exercise 4

# # # print all odd numbers from 1 to 20
for i in range(1, 21):
    if i % 2 != 0:
        print(i)  # --> 1st way


for i in range(1, 21, 2):
    print(i)  # --> 2nd way


# print the table of 57

for i in range(1, 11):
    print(f'57 x {i} = {57 * i}')


# print all the multiples of 3 from 1 to 50 but skip 15


for i in range(1, 51):
    if i != 15:
        continue
    elif i % 3 == 0:
        print(i)


# take teo integers a and b as input then find and print the fist number betwwen 1 to 1000 that is devisible by both a and b

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print(
            f"The first number between 1 and 1000 that is divisible by both {a} and {b} is: {i}")
        break
