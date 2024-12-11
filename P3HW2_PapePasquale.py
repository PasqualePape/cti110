# Pasquale Pape
# 10/23/2024
# P3HW2
# Calculate reg and OT pay for employee

'''
Input: Get name from user as string
Input: Get number of hours worked as int
Input: Get reg pay rate as float

Output: dotted line and employee name

If employee has OT(more then 40 hours worked)
Calculate: OT hours(hours worked - 40)
Calculate: OT payrate reg * 1.5
Determine: how many regular hours worked-has to be 40
Calculate: pay for reg hours(pay rate * 40)
Calculate: OT pay(OT hours * OT pay rate
Calculate: gross pay(reg pay + overtime pay)



else: has no overtime
hours worked is the original value
pay rate is same
OT hours is 0
OT pay rate is 0
Calculate: pay for reg hours(hours worked * reg pay rate)
'''
name = (input("Enter employee's name: "))
hrW = int(input("Enter number of hours worked: "))
ePr = float(input("Enter employee's pay rate: "))
otH = float(0.0)
otPr = float(0.0)
otP = float(0.0)
rhP = float(0.0)
grossp = float(0.0)

if hrW > 40:
    otH = hrW - 40
    otPr = ePr * 1.5
    otP = otH * otPr
    rhP = ePr * 40
    
else: rhP = ePr * hrW 
grossp = rhP + otP


print("---------------------------------------")
print(f"Employee's name:    {name}")
print() 
print("Hours Worked    Pay Rate    OverTime    OverTime Pay        RegHour pay         Gross Pay")
print("---------------------------------------------------------------------------------------------------")
print(f"{hrW:.1f}            {ePr:.1f}        {otH:.1f}         {otP:.2f}              ${rhP:.2f}             ${grossp:.2f}   ")



#print(f"hours worked:{hrW}   payrate:{ePr}   overtime:{otH}   overtime pay:{otP}   regular pay:{rhP}   gross pay:{grossp}")




