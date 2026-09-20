# mini calcultor

print("Welcome to the mini calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /,**): ")


if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")

elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")

elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "**":
    result = num1 ** num2
    print(f"The result of {num1} ** {num2} is: {result}")
