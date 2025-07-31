# Basic Calculator Program

# Ask the user for two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

# Ask the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the chosen operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")

else:
    print("Invalid operation! Please choose +, -, *, or /.")
