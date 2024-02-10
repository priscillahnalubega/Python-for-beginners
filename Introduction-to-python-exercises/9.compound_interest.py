"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
"""
p = float(input("Enter your principal amount in $: "))
r= 4/100

for t in range(1, 4):
    total_amount = p * (1 + r) ** t
    print(f"The total amount after {t} year{'s' if t > 1 else ''} is ${total_amount:.2f}")


