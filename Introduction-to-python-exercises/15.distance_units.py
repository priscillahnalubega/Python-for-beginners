"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don't have them memorized.
"""
#Constants for convertion
FEET_TO_INCHES = 12
FEET_TO_YARDS = 1/3
FEET_TO_MILES = 1 / 5280


#Ask for user input
user_distance = float(input("Enter measurement in feet: "))

#Convert measurements to inches, yards,and miles
inches = user_distance * FEET_TO_INCHES
yards = user_distance * FEET_TO_YARDS
miles = user_distance * FEET_TO_MILES

#Display the measurements to inches,yards, and miles
print(f"The measurement in inches is {inches:.2f}inches")
print(f"The measurement in yards is {yards: .2f}yards")
print(f"The measurement in miles is{miles: .6f}miles")