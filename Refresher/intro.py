"""
High level , interprted programmming language known for its readability and simplicity.
used for data analysis, web development, scientific computing etc.
num1 = input ("Enter a number1 :")
num2 = input ("Enter a number2 : ")

sum = int (num1) + int(num2) 

print (f"The sumation of {num1} and {num2} is : {sum} ")

# Explicit joining
result = 10 + 20 + 40 + 50 + \
         30 + 40 + 60
print(result)

#implicit joining 
result = ( 40 + 50 + 60 +
           0 + 59)
print (result)

#Identation
Fox  = 1
if Fox ==1:
    print("This is a fox ")

# Variables and Data types
name =" Alice"
age = 24
school = "Makerere University"
district =  "Kampala"

print (f"hello {name} aged {age} who goes to {school} and lives in {district}")

# Control Structures
while True:
    age = input("Enter your age : ")
    if int(age) >= 18:
        print ("You are eligible to vote ")
        break
    else:
      print("You are not eligible")

# continue statement 
for i in (1,6):
    if i == 3:
      continue
print (i)

# Area of rectangle 
length = float(input("Enter a number: "))
width = float(input("Enter another number:"))

area = length * width

print (f"The area of the rectangle is {area}")
"""
# Write a program that tells whether the number is even or odd
a = int(input("Enter a number: "))

if a % 2 == 0:
    print(f"{a} is an even number")
else:
    print(f"{a} is an odd number")

# Functions and forms

