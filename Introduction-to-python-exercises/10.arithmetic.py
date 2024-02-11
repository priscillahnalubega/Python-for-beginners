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
#The function for sum
def sum(a,b):
    return a+b

#the function for difference
def difference(a,b):
    return a - b
#the function for multiplication
def product(a,b):
    return a*b
#the function for divition
def quotient (a,b):
    if b == 0:
        return "Cannot be divided by zero "
    else:
        return a / b
#the function for remainder 
def remainder(a,b ):
    if b == 0:
        return "Cannot be divided by zero "
    else:
        return a % b
# the function for The result of log10 a
def log(a):
    return  log10(a)
#the function for the result of ab
def ab(a,b):
    return ab

#Main calculator while loop
while True:
    #Print Options to user
    print("Options:")
    print("Enter 'add'to get the sum")
    print("Enter 'subtract' to get the difference ")
    print("Enter 'multiply' to get the product")
    print("Enter 'divide' to get the quotient")
    print ("Enter 'remainder' to get the remainder")
    print("Enter 'log' to get log10 a")
    print("Enter 'ab' to get ab")
    print("Enter 'quit' to end the program")

    #Ask for user input

    user_input = input(': ').lower()

    #check if the user wants to exit the program
    if user_input == 'quit':
       break

