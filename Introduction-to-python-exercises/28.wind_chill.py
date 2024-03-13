"""
When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.
In 2001, Canada, the United Kingdom and the United States adopted the following formula for computing the wind chill index. Within the formula Ta is the
air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used with temperatures in
degrees Fahrenheit and wind speeds in miles per hour.
WCI = 13.12 + 0.6215Ta - 11.37V**0.16 + 0.3965Tav**0.16
Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer.
The wind chill index is only considered valid for temperatures less than or
equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per
hour.
"""

# Get user input
V = float(input("Enter the speed of the wind in Km/hr: "))
Ta = float(input("Enter the temperature of air in Degree Celcius: "))

# Check for validity of the conditions
if Ta <= 10 and V > 4.8:
    # Calculating the wind Chill index correctly
    WCI = 13.12 + (0.6215 * Ta) - 11.37 * (V ** 0.16) + 0.3965 * Ta * (V ** 0.16)
    # Displaying the Wind Chill Index to the closest integer
    print(f"The wind chill index is: {round(WCI)}")
else:
    print("The wind chill index is not valid for the entered temperature and wind speed.")
