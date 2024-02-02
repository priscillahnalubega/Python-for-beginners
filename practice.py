#problem1: find the value of 2+3
print (2+3)

#problem2: print Hello world!  four times 
print ("Hello world"*4)

#Create a python script with the following text and see the output
1 + 2
#If it doesn’t print anything, what changes can you make to the program to print the value?
print( 1+2)

# What will be output of the following program?
x = 4
y = x +1
x = 2
print (x,y)

#what will be the output of the following program
x, y = 2, 6
x, y = y, x+2
print (x,y)

#What will be the output of the following program
a, b = 2, 3
c = a
b = c + 1

print(a, b, c)

#Functions
def square(x):
    return x*x
square (5)

"""
#OOP
Exercise: Bank Account Class
Objective: Create a BankAccount class to represent a user's bank account. It should allow deposits, withdrawals, and provide the account balance.

Step 1: Define the Class
Attributes:

account_holder: The name of the account holder.
balance: The current balance of the account (initialized to zero).
Methods:

deposit(amount): Method to add funds to the account. It should also print the amount deposited and the new balance.
withdraw(amount): Method to subtract funds from the account if sufficient balance exists. It should also print the amount withdrawn and the new balance.
get_balance(): Method to print the current balance.
Step 2: Create and Test the Class
Create an instance of BankAccount for a user.
Perform some deposits and withdrawals.
Check the balance.
Example Code Structure

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        # Add code for deposit

    def withdraw(self, amount):
        # Add code for withdrawal

    def get_balance(self):
        # Add code to display balance

# Testing the class
account = BankAccount("Alice")
account.deposit(100)
account.withdraw(50)
account.get_balance()
"""
# Solution
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Dear {self.account_holder}, you have deposited {amount}. Your new balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Dear {self.account_holder}, you have withdrawn {amount}. Your new balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"The current balance is {self.balance}.")

# Testing the class
account = BankAccount("Alice")
account.deposit(100)
account.withdraw(50)
account.get_balance()
"""
#Exercise: Rectangle Class
Objective: Create a Rectangle class that represents a rectangle and can calculate its area and perimeter.

Step 1: Define the Class
Attributes:

length: The length of the rectangle.
width: The width of the rectangle.
Methods:

area(): Method to calculate and return the area of the rectangle.
perimeter(): Method to calculate and return the perimeter of the rectangle.
Optionally, a method to represent the rectangle's details as a string (like __str__).
Step 2: Create and Test the Class
Create an instance of Rectangle with specific length and width.
Calculate and print the area and perimeter of the rectangle.

"""
class Rectangle:
     def __init__(self,length, widith):
         self.length = length
         self.widith = widith
     
     def area(self):
         return self.length * self.widith
     def perimeter(self):
         return 2*self.length + 2*self.widith
     
rectangle1 = Rectangle(100, 30)
print(rectangle1.area())
print(rectangle1.perimeter())