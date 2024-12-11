# Pasquale Pape
# 10/2/2024
# P2LAB2
# using dictonaries

#creating dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
print()
#priting keys
print(cars.keys())
print()
#get a car(key) from the user
userCar = input("Enter a vehicle to see its mpg: ")
print()
#display mpg from users car
print(f"The {userCar} gets {cars[userCar]} mpg.")
print()
#get number of miles from user
mtd = int(input(f"how many miles would you like to drive the {userCar}? "))
print()
#calculate gallons of gas needed
gallons_needed = mtd/cars[userCar]
#display galolons of gas needed
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {userCar} {mtd} miles.")
