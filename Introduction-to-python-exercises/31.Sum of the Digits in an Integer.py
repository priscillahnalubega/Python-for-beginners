"""
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.                
"""
# Ask for user input
user_input = input("Enter a four-digit integer: ")

# Validate input
if len(user_input) == 4 and user_input.isdigit():
    
    digits = [int(digit) for digit in user_input]
    sum_of_digits = sum(digits)
    
    # Prepare the string to display the equation
    equation = " + ".join(user_input) + f" = {sum_of_digits}"
    
    # Display the sum of the digits along with the equation
    print(f"The sum of the digits is: {equation}")
else:
    print("Invalid input. Please make sure you enter a four-digit integer.")

