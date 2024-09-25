 # Pasquale Pape
 # 9/25/2024
 # P1HW2 
 # a program that does some basic math on numbers that are entered.

print("This program calculates and displays travel expenses")
print()
# getting user input
budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
# printing out input
print()
print("------------------Travel Expenses------------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accomodation: {hotel}")
print(f"Food: {food}")
print()
# calculating remaining 
remaining = budget - (gas + hotel + food)
print(f"Remaining Balance: {remaining}")
