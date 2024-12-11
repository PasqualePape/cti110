 #Pasquale Pape

 #Dat10/13/2024

 #P2HW2

 #Takes user input and displays a list with information

#make list
GradeList = []

#get grades as separate statements 

grade1 = input("Enter grade for module 1: ")
grade2 = input("Enter grade for module 2: ")
grade3 = input("Enter grade for module 3: ")
grade4 = input("Enter grade for module 4: ")
grade5 = input("Enter grade for module 5: ")
grade6 = input("Enter grade for module 6: ")
#add grades to list

GradeList.append(float(grade1))
GradeList.append(float(grade2))
GradeList.append(float(grade3))
GradeList.append(float(grade4))
GradeList.append(float(grade5))
GradeList.append(float(grade6))
print()
print("--------------Results--------------")
#get sum as a statement 
sum_list = sum(GradeList)

#displaying min,max and sum of grades
print(f"Lowest Grade: {min(GradeList):.1f}")
print(f"Highest Grade: {max(GradeList):.1f}")
print(f"Sum of Grades: {sum_list:.1f}")

#getting average of grades
average = sum_list / 6

#displays average 
print(f"Average: {average:.2f}")
print("-------------------------------------------------")