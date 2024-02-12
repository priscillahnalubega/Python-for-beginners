"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units
"""
def MPG_to_l_per_100km (MPG):
    return 235.214583 / MPG

MPG = float(input("Enter fuel efficiecy in MPG:"))

l_per_100km = MPG_to_l_per_100km

print(f"The equivalent fuel efficiency in l_per_100km is {l_per_100km:.2f} 1/100km")