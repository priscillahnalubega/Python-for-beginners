"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
due to gravity is 9.8m/s2. You can use the formula vf = vi2 + 2ad to compute the
final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known.
"""
from math import sqrt
# Computation constants

acceleration_due_gravity = 9.8 
initial_speed = 0

# Ask for user input

user_distance = float(input("Enter the user_input  : "))

# Calculate the final speed 

final_speed = sqrt(initial_speed**2 + 2* acceleration_due_gravity*user_distance)

# Display the final speed

print(f"The final speed is {final_speed : .1f} m/s")