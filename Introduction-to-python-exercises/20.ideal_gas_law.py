"""
The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 mol K J , and T is the
temperature in degrees Kelvin.

Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit.

Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
multiply it by 5 9 and then add 273.15 to it.
"""

# The computation constant
IDEAL_GAS_CONSTANT =  8.314

# Ask for user input
user_pressure = float(input("Enter the pressure in pascals: "))
user_volume = float(input("Enter the volume litres: "))
user_temperature = float(input("Enter the temperature in degrees Celsius: "))

# Temperature conversion from Celsius to Kelvin
user_temperature_in_kelvin = user_temperature + 273.15

# Computing  the amount of gas in moles
amount_of_gas_in_moles = (user_pressure * user_volume)/ (IDEAL_GAS_CONSTANT * user_temperature_in_kelvin)

# Displaying the amount of gas in moles

print(f"The amount of gas in moles is {amount_of_gas_in_moles: .2f} moles")
