"""
Write a programm that asks the user to enter the width and length of a room. Once the values have been read, your program should compute and display the area of the room.The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""
Units = "m"
length = float(input(f"Enter the length in meters in {Units}:"))
width = float(input(f"Enter the width in {Units}: " ))

Room_Area = length * width 

print(f"{Room_Area} square {Units}")