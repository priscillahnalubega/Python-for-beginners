"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material's specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

Hint: The specific heat capacity of water is 4.186 J
g◦C. Because water has a density of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
in this exercise.
Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.

Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise.

"""
# Calculation constants
SPECIFIC_HEAT_CAPACITY_OF_WATER = 4.18
COST_PER_KILOWATT_HOUR = 0.089  # 8.9 cents
JOULES_TO_KILOWATT_HOURS = 1 / 3600000  # 1 kWh = 3,600,000 Joules


#Ask for user input
user_mass = float(input("Enter the mass of water in g: "))
user_tempeature_change = float(input("Enter the temperature in celcius degrees: "))

#Computing the  total amount of energy in joules
total_amount_of_energy = user_mass * SPECIFIC_HEAT_CAPACITY_OF_WATER * user_tempeature_change

# Display the total amount of energy in joules
print(f"The toatal amount of energy required to be removed or added is : {total_amount_of_energy: .2f} joules ")

#Calculating the cost of heating the water
energy_in_kWh = total_amount_of_energy * JOULES_TO_KILOWATT_HOURS
cost = energy_in_kWh * COST_PER_KILOWATT_HOUR

#Display the amount of energy and cost.
print(f"The total amount of energy required to achieve the temperature change is: {total_amount_of_energy:.2f} Joules.")
print(f"The cost of boiling the water for a cup of coffee is: ${cost:.4f}")
