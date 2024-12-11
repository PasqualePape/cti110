 # Pasquale Pape

 # 10/21/2024

 # P3LAB

 # calculate the most efficient coin combanation

#get amount of money from user as float
money = float(input("Enter the amount of money as a float: $"))

#Conver money to a whole number
money = round(money * 100)

#if no change
if money ==0:
    print("No change")

#money = int(money * 100)
#print(money)

#get whole dollars from money amount
dollars = money // 100
#print(dollars)

#remove the dollar amount from money
money = money - (dollars * 100)
#print(money)

#get quarters from money amount
quarters = money // 25

#remove the quarter amount from money
money = money - (quarters * 25)

#get dimes from money amount
dimes = money // 10

#remove the dimes amount from money
money = money - (dimes * 10)

#get nickels from money amount
nickels = money // 5

#remove the nickels amount from money
money = money - (nickels * 5)

#get pennies from money amount
pennies = money

#print(f"Dollars = {dollars} quarters = {quarters} dimes = {dimes} nickels = {nickels} pennies = {pennies}")

#displayes number of dollars, quarters, dimes, nickels and pennies 
if dollars >=1:
    if dollars == 1:
        print(f"{dollars} dollar")
        #else more then one dollar
    else: print(f"{dollars} dollars")

if quarters >=1:
    if quarters == 1:
        print(f"{quarters} quarter")
        #else more then one quarter
    else: print(f"{quarters} quaters")

if dimes >=1:
    if dimes == 1:
        print(f"{dimes} dime")
        #else more then one dime
    else: print(f"{dimes} dimes")
    
if nickels >=1:
    if nickels == 1:
        print(f"{nickels} nickel")
        #else more then one nickel
    else: print(f"{nickels} nickels")

if pennies >=1:
    if pennies == 1:
        print(f"{pennies} penny")
        #else more then one penny
    else: print(f"{pennies} pennies")
















