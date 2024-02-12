"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
A one dollar coin was introduced in Canada in 1987. It is referred to as a
loonie because one side of the coin has a loon (a type of bird) on it. The two
dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
derived from the combination of the number two and the name of the loonie.
"""
# Read the amount in cents from the user
amount = int(input("Enter the amount of change in cents: "))

print("The change will be given as:")

# Calculate the number of toonies
toonies = amount // 200
amount = amount % 200
print(f"Toonies: {toonies}")

# Calculate the number of loonies
loonies = amount // 100
amount = amount % 100
print(f"Loonies: {loonies}")

# Calculate the number of quarters
quarters = amount // 25
amount = amount % 25
print(f"Quarters: {quarters}")

# Calculate the number of dimes
dimes = amount // 10
amount = amount % 10
print(f"Dimes: {dimes}")

# Calculate the number of nickels
nickels = amount // 5
amount = amount % 5
print(f"Nickels: {nickels}")

# The remainder is the number of pennies
pennies = amount
print(f"Pennies: {pennies}")
