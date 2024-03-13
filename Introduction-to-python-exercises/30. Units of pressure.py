"""
In this exercise you will create a program that reads a pressure from the user in kilopascals. Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""
#Get user input
User_pressure = float(input("Enter pressure in kilopascals: "))

#Conversions into pounds per square inch, millimeters of mercury and atmospheres
Pressure_in_pounds_per_square_inch = 0.145038 * User_pressure
Pressure_in_millimeters_of_mercury =  7.50062 * User_pressure
Pressure_in_atmospheres = 0.00986923 * User_pressure

#Displaying presure in Pounds per square inch, millimeters of mercury and atmospheres
print(f"The pressure in pounds per square inch is {Pressure_in_pounds_per_square_inch: .2F}psi. \n The pressure in millimeters of mercury is {Pressure_in_millimeters_of_mercury: .2f}mmHg. \n The pressure in atmosphere is {Pressure_in_atmospheres: .2f}atm.")