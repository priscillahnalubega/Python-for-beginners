"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum =
((n)(n + 1))/2

"""
while True:
    n  = int(input("Enter a positive integer: "))
    if n> 0:
        sum = ((n)*(n + 1))/2
        print(f"The sum is :{sum}")
        break
    else:
        print("The number you entered is not a positive number, please enter a positive number.")