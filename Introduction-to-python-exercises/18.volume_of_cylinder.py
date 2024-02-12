"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place
"""

from math import pi

#Ask input from the user 
user_radius = float(input("Enter the radius: "))
user_height = float(input("Enter the height: "))

#Computation of the volume of the cylinder
volume_of_cylinder = pi* (user_radius**2 ) * user_height

#Display volume of the cylinder

print(f"The volume of the cylinder is : {volume_of_cylinder}")
