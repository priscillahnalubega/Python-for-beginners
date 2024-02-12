"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
The value 6371.01 in the previous equation wasn’t selected at random. It is
the average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
"""

from math import sin , cos,acos, radians

def points(t1, g1, t2, g2):
    # converting degrees to radians
    t1_rad = radians(t1)
    g1_rad = radians(g1)
    t2_rad = radians(t2)
    g2_rad = radians(g2)
    # Calculate the distance
    
    distance = 6371.01 * acos(sin(t1_rad) * sin(t2_rad) + cos(t1_rad) * cos(t2_rad) * cos(g1_rad - g2_rad))
    return distance
#getting user input
print("Enter the latitude and longitude for two points on the Earth.")
t1 = float(input("Latitude of point 1 (degrees): "))
g1 = float(input("Longitude of point 1 (degrees): "))
t2 = float(input("Latitude of point 2 (degrees): "))
g2 = float(input("Longitude of point 2 (degrees): "))

#calculate the distance
distance = points(t1, g1, t2, g2)
print(f"The distance between the two points, following the surface of the Earth, is: {distance:.2f} kilometers.")




