"""
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:

area = (n * s**2)/(4*( tan (pi/n)))

Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values
"""
from math import tanh, radians, pi

#Ask user input 
s = float(input("Enter the sides length in cm: "))
n = float(input("Enter the angle in degrees: "))

#Converting degrees to radians
n_rad = radians(n)

#Computations
area = (n_rad * s**2)/(4*( tanh(pi/n_rad)))

#Display the area
print("The area of a regular polygon is : {area:.2f} cm²")
 
