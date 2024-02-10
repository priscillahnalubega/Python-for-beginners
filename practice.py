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

""" 

### Exercise: Movie Theater Seat Booking System

**Objective**: Create a `Theater` class that represents a small movie theater. The theater will have a fixed number of seats, and you should be able to book a seat, check if a seat is available, and cancel a booking.

#### Step 1: Define the Class
1. **Attributes**:
   - `seats`: A list or dictionary to represent the seats in the theater. Each seat can be either "available" or "booked".

2. **Methods**:
   - `book_seat(seat_number)`: Method to book a specific seat if it's available. If the seat is already booked, print a message indicating that the booking is unsuccessful.
   - `cancel_booking(seat_number)`: Method to cancel the booking of a specific seat.
   - `check_availability(seat_number)`: Method to check if a specific seat is available.
   - `get_available_seats()`: Method to return the number of available seats.

#### Step 2: Create and Test the Class
- Create an instance of `Theater` with a certain number of seats.
- Perform some bookings and cancellations.
- Check the availability of specific seats and the total number of available seats.

#### Example Code Structure
```python
class Theater:
    def __init__(self, total_seats):
        # Initialize the seats

    def book_seat(self, seat_number):
        # Add code to book a seat

    def cancel_booking(self, seat_number):
        # Add code to cancel a booking

    def check_availability(self, seat_number):
        # Add code to check if a seat is available

    def get_available_seats(self):
        # Add code to get the number of available seats

# Testing the class
theater = Theater(20)  # A theater with 20 seats
theater.book_seat(5)
theater.cancel_booking(10)
print(f"Available seats: {theater.get_available_seats()}")
```

"""

class Theater:
    def __init__(self, total_seats):
        self.seats = ["available"] * total_seats

    def book_seat(self, seat_number):
        if self.seats[seat_number] == "available":
            self.seats[seat_number] = "booked"
            print(f"Seat {seat_number} successfully booked.")
        else:
            print(f"Seat {seat_number} is already booked.")

    def cancel_booking(self, seat_number):
        if self.seats[seat_number] == "booked":
            self.seats[seat_number] = "available"
            print(f"Booking for seat {seat_number} cancelled.")
        else:
            print(f"Seat {seat_number} is already available.")

    def check_availability(self, seat_number):
        return "available" if self.seats[seat_number] == "available" else "booked"

    def get_available_seats(self):
        return self.seats.count("available")

# Testing the class
theater = Theater(20)
theater.book_seat(5)
theater.cancel_booking(10)
print(theater.check_availability(5))
print(f"Available seats: {theater.get_available_seats()}")

# Let's consider a small project where we can use classes, objects, and inheritance. How about a simple system to manage a library? We can have a base class representing `Books`, and derived classes for different genres like `Fiction`, `NonFiction`, etc., each with some specific attributes or methods.

class Book:
    def __init__(self,title, author, isbn):
        self.title =title
        self.author = author
        self.isbn = isbn
        
    def display_info(self):
        return f"{self.title} by {self.author} with {self.isbn}"
    
class Fiction(Book):
    def __init__(self, title, author,isbn, genre):
        super().__init__(title,author,isbn)
        self.genre = genre
    def display_info(self):
        return f"{super().display_info()}, Genre: {self.genre}"
    
class NonFiction(Book):
    def __init__(self, title, author,isbn, subject):
        super().__init__(title,author,isbn)
        self.subject = subject
    def display_info(self):
        return f"{super().display_info()}, Subject: {self.subject}"

# Creating book instances
fiction_book = Fiction("1984", "George Orwell", "123456789", "Dystopian")
nonfiction_book = NonFiction("A Brief History of Time", "Stephen Hawking", "987654321", "Science")

# Displaying book information
print(fiction_book.display_info())
print(nonfiction_book.display_info())


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

# Practical python exercises