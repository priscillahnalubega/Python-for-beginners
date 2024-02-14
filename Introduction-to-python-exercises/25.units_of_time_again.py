"""
In this exercise you will reverse the process described in the previous exercise.

Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary.
"""
# Constants for conversion
SECONDS_IN_A_MINUTE = 60
MINUTES_IN_AN_HOUR = 60
HOURS_IN_A_DAY = 24
SECONDS_IN_AN_HOUR = SECONDS_IN_A_MINUTE * MINUTES_IN_AN_HOUR
SECONDS_IN_A_DAY = SECONDS_IN_AN_HOUR * HOURS_IN_A_DAY

# Ask user input
total_seconds = int(input("Enter the number of seconds: "))

# Calculating days, hours, minutes, and seconds
days = total_seconds // SECONDS_IN_A_DAY
hours = (total_seconds % SECONDS_IN_A_DAY) // SECONDS_IN_AN_HOUR
minutes = (total_seconds % SECONDS_IN_AN_HOUR) // SECONDS_IN_A_MINUTE
seconds = total_seconds % SECONDS_IN_A_MINUTE

# Formatting the output to ensure two digits for hours, minutes, and seconds
formatted_time = f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}"

# Display the formatted time
print(f"The equivalent amount of time is: {formatted_time}")
