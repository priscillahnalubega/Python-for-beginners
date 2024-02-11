
# Basic calculator project
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator loop
while True:
    # Display menu to user
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(': ').lower()  # Convert input to lowercase to make the check case-insensitive

    # Check if the user wants to exit the program
    if user_input == 'quit':
        break

    # Check for valid input and perform desired operation
    if user_input in ('add', 'subtract', 'divide', 'multiply'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == 'add':
            result = add(num1, num2)
        elif user_input == 'subtract':
            result = subtract(num1, num2)
        elif user_input == 'divide':
            result = divide(num1, num2)
        elif user_input == 'multiply':
            result = multiply(num1, num2)

        print("Result: " + str(result))
    else:
        print("Enter a valid operation.")