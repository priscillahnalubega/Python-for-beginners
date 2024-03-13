"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
"""
#Ask for user input
Temperature_in_celsius = float(input("Enter temperature in degrees celsius: "))

#Converting Temperature from degrees celcius to degrees fahrenheit
Temperature_in_Fahrenheit = (9/5 *Temperature_in_celsius ) + 32
Temperature_in_Kelvin = 273.15 + Temperature_in_celsius

#Diplaying in degree Fahrenheit and Kelvins
print(f"The temperature in Fahrenheit is {Temperature_in_Fahrenheit: .2F}˚F and in Kelvin is {Temperature_in_Kelvin: .2F}K")