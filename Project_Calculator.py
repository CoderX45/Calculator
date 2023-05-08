import math

# This project was created on top of a very simple calculator I did a few years ago that was only able to do addition and subtraction.
# Thus I only used my prior knowledge, skills learnt on this course and for error handling also parts from "learnpython.org"
# I added 3 more operations which also require some additional levels of error handling due to how maths works.

# Defining of functions that are used in the calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square_root(x):
    return math.sqrt(x)

# Asking for the user's name
name = input("Welcome to this simplified calculator! Please enter your name: ")
print("Welcome", name, "! Let's get calculating!\n")

# Looping the calculator to keep running until the user does not want/need to calculate anymore
while True:
    # Display of menu
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")

    # Asking for user's choice of operation
    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4', '5']:
            break
        else:
            print("Invalid input. Please enter a number from 1 to 5.")

    num1 = None
    while num1 is None:
        num1_str = input("Enter first number: ")
        try:
            num1 = float(num1_str)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if choice != '5':
        # Asking the user to enter the second number and check for division by zero (is not possible and results in an error)
        num2 = None
        while num2 is None:
            num2_str = input("Enter second number: ")
            try:
                num2 = float(num2_str)
                if choice == '4' and num2 == 0:
                    print("Error: Division by zero")
                    num2 = None
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    else:
        num2 = None

    # Calling the appropriate function based on the user's choice
    if choice == '1':
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)

    elif choice == '2':
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result)

    elif choice == '3':
        result = multiply(num1, num2)
        print(num1, "*", num2, "=", result)

    elif choice == '4':
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)

    elif choice == '5':
        result = square_root(num1)
        print("Square root of", num1, "is", result)

    else:
        print("Invalid input")
        continue

    # Continuation of the loop (asking for more calculations)
    # If user decides to not keep calculating, the calculater prints a thank you message and basically "shuts down"
    while True:
        more_calculations = input("Do you want to calculate more? (yes/no): ")
        if more_calculations.lower() == "yes" or more_calculations.lower() == "no":
            break
        else:
            print("Invalid input. Please enter either 'yes' or 'no'.")

    if more_calculations.lower() != "yes":
        print("Thank you for testing me out,", name,"!")
        break

#

