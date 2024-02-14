"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration
"""
#Computation constants
SECONDS_IN_A_MINUTE = 60
MINUTES_IN_AN_HOUR = 60
HOURS_IN_A_DAY = 24

# Ask user input 
number_of_days = float(input("Enter number of days: "))
hours = float(input("Enter number of hours: "))
minutes = float(input("Enter number of minutes: "))
seconds = float(input("Enter number of seconds: "))

# Computing the total number of seconds represented
seconds_in_an_hour = SECONDS_IN_A_MINUTE * MINUTES_IN_AN_HOUR
seconds_in_a_day = HOURS_IN_A_DAY * seconds_in_an_hour

total_number_of_seconds = (number_of_days * seconds_in_a_day) + (hours * seconds_in_an_hour)+ (minutes * SECONDS_IN_A_MINUTE) + seconds

#Display the total number of seconds represented

print(f"The total number of seconds is {int(total_number_of_seconds)}")
