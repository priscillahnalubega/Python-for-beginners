"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.
"""
# Constants
BREAD_PRICE = 3.49
DISCOUNT_RATE = 0.60  

# Ask for user input
number_of_day_old_bread = int(input("Enter number of day-old bread loaves: "))

# Calculations
regular_price = BREAD_PRICE * number_of_day_old_bread
discount_amount = regular_price * DISCOUNT_RATE
total_price = regular_price - discount_amount

# Display results with two decimal places and aligned decimals
print(f"Regular price of bread: ${regular_price:7.2f}")
print(f"Discount:                -${discount_amount:7.2f}")
print(f"Total price:            ${total_price:7.2f}")
