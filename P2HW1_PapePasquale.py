 # Pasquale Pape
 # 10/7/2024
 # P1HW2 
 # Changing the output of P1HW2

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
print(f"{'Location:':<25} {destination}")
print(f"{'Initial Budget:':<25} ${float(budget):.2f}")
print(f"{'Fuel:':<25} ${float(gas):.2f}")
print(f"{'Accomodation:':<25} ${float(hotel):.2f}")
print(f"{'Food:':<25} ${float(food):.2f}")
print("---------------------------------------------------")
# calculating remaining 
remaining = budget - (gas + hotel + food)
print(f"Remaining Balance: ${remaining:.2f}")

