 # Pasquale Pape
 # 9/30/2024
 # P2LAB1
 # Using imported library, math, and f-string
import math

#get radius from user
r = float(input("what is the radius of the circle? "))
print()

#calculate diameter
d = 2 * r
 
#display diameter with one decimal place
print(f"The diameter of the circle is {d:.1f}")
print()

#calculate circumference
c = 2 * math.pi * r

#display circumference with two decimal places
print(f"The circumference of the circle is {c:.2f}\n")

 #calculate the area
a = math.pi * r **2

#display the area
print(f"The area of the circle is {a:.3f}")
