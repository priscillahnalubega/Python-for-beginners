"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd
"""
#Ask for user input
user_integer = int(input("Enter any integer: "))

# validation
if  user_integer %2  == 0:
    print(f"The integer {user_integer} is even")
else:
    print(f"The integer {user_integer} is odd ")
