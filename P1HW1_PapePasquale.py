# Pasquale Pape
# 9/16/2024
# P1HW1 
# code that collects information from user, processes information collected and display results to user.

print("-------Calculating Exponents-------")
print()
print()
#get input into int
base_value = int(input("Enter an interger as the base value: "))

#get input into int
exponent = int(input("Enter an integer as the exponent: "))
print()
#display math to user
print(base_value, "raised to the power of", exponent, "is", base_value**exponent, "!!")
print()
print()
#Get int from user for addition and subtraction
print("-------Addition and Subtraction-------")
print()
print()
#get input into int
start_num = int(input("Enter a starting integer:"))

#get input into int
add_num = int(input("Enter an integer to add:"))

#get input into int
sub_num = int(input("Enter an integer to subtract:"))
print()
print()
#calculate the result
result = start_num + add_num - sub_num
#display result
print(start_num, "+", add_num, "-", sub_num, "is equal to", result)
