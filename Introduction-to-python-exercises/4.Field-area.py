"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
"""
Units = "ft"
Units1 = "arcs"
length = float(input(f"Enter the length in {Units}:"))
width = float(input(f"Enter the width in {Units}: "))

Field_area = (length * width)/ 43560

print(f"{Field_area} square {Units1}")



