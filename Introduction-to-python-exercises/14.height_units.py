"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters
"""
# Constants for conversion
ONE_FOOT_TO_INCHES = 12
ONE_INCH_TO_CM = 2.54

# Read the user's height in feet and inches
feet = float(input("Enter your height - Feet part: "))
inches = float(input("Enter your height - Inches part: "))

# Convert the height to centimeters
total_inches = (feet * ONE_FOOT_TO_INCHES) + inches
height_cm = total_inches * ONE_INCH_TO_CM

# Display the height in centimeters
print(f"Your height in centimeters is: {height_cm:.2f} cm")

