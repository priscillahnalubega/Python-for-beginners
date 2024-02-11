"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab
Hint: You will probably find the log10 function in the math module helpful
for computing the second last item in the list
"""
from math import log10

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Cannot be divided by zero" if b == 0 else a / b

def modulo(a, b):
    return "Cannot be divided by zero" if b == 0 else a % b

def logarithm(a):
    return log10(a) if a > 0 else "Logarithm undefined for non-positive values"

def exponentiation(a, b):
    return a ** b

# Main program loop
while True:
    print("\nOptions:")
    print("Enter 'add' to get the sum")
    print("Enter 'subtract' to get the difference")
    print("Enter 'multiply' to get the product")
    print("Enter 'divide' to get the quotient")
    print("Enter 'remainder' to get the remainder")
    print("Enter 'log' to get the log10 of the first number")
    print("Enter 'exp' to get a raised to the power of b")
    print("Enter 'quit' to end the program")

    user_input = input(": ").lower()

    if user_input == 'quit':
        print("Goodbye!")
        break

    if user_input in ('add', 'subtract', 'multiply', 'divide', 'remainder', 'log', 'exp'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == 'add':
            result = add(num1, num2)
        elif user_input == 'subtract':
            result = subtract(num1, num2)
        elif user_input == 'multiply':
            result = multiply(num1, num2)
        elif user_input == 'divide':
            result = divide(num1, num2)
        elif user_input == 'remainder':
            result = modulo(num1, num2)
        elif user_input == 'log':
            result = logarithm(num1)
        elif user_input == 'exp':
            result = exponentiation(num1, num2)

        print("Result: " + str(result))
    else:
        print("Invalid operation. Please try again.")

