"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
"""
def refund (litres,number_of_bottles):
    if litres <= 1:
     deposit = 0.10 * number_of_bottles
    else:
       deposit = 0.25 * number_of_bottles
    return deposit 

number_of_small_bottles = int(input("Enter the number number of small_bottles: "))
number_of_large_bottles = int(input("Enter number of large_bottles: "))

Total_refund = refund(1,number_of_small_bottles) + refund(3,number_of_large_bottles)

print(f"The total refund will be : ${Total_refund:.2f}")