"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value
"""
# Read three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Find the smallest and largest values
smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

# Find the middle value
middle = (num1 + num2 + num3) - smallest - largest

# Display the numbers in sorted order
print("The numbers in sorted order are:", smallest, middle, largest)
