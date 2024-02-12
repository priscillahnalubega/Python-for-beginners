"""
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr**2. The
volume of a sphere is computed using the formula volume = 4/3πr**3
"""
from math import pi 
#Ask input from a user
user_radius =  float(input("Enter the radius of the circle: "))

#computing area of the circle  and volume of the sphere
area = pi* user_radius**2
volume = (4/3)* pi *user_radius **3

#Displaying  area and circle volume

print(f"The area of the circle is : {area: .2f}")
print(f"The volume of the sphere is : {volume: .2f}")
