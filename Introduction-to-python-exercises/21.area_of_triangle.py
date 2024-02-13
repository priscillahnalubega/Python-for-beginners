"""
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area = 1/2 b * h

Write a program that allows the user to enter values for b and h. The program
should then compute and display the area of a triangle with base length b and height h.
"""
#Ask user input 
user_base = float(input("Enter the base of the triangle in cm: "))
user_height = float(input("Enter the height of the triangle in cm: "))

#Compute the area of the triangle
area_of_the_triangle = 1/2 * user_base * user_height

#Display the area of the triangle
print(f"The area of the triangle is {area_of_the_triangle: .2f}square cm")
