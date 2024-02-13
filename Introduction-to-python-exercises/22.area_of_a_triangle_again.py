"""
)
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
area = sqrt(s * (s - s1) * (s - s2) *  (s - s3))
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area
"""
from math import sqrt
#Ask user input
s1 = float(input("Enter the side s1 in cm: "))
s2 = float(input("Enter the side s2 in cm: "))
s3 = float(input("Enter the side s3 in cm: "))

#Computations
s = (s1 + s2 + s3)/2
area = sqrt(s * (s - s1) * (s - s2) *  (s - s3))

#Display the area
print(f"The area of a triangle with sides {s1} cm, {s2} cm, and {s3} cm is: {area:.2f} cm²")

