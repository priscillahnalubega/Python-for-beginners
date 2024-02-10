"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.

"""
widget = 75
gizmo = 112

number_of_gizmos = int(input("Enter the number of gizmos in grams: "))
number_of_widgets = int(input("Enter the number of widgets in grams: "))

total_weight = (widget * number_of_widgets) + (gizmo * number_of_gizmos)

print("The total weight is : {total_weight} grams")