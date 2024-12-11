#Pasquale Pape
#11/4/2024
#P4HW1
#Enter in grades using a loop and list then display the lowest score and drop it

#get input from user for how many scores are needed
scores = int(input("How many scores do you want to enter? "))
#empty list to store grades
grades = []
#for loop to get grades
for grade in range(0, scores):
    score = float(input(f"Enter score #{grade+1}: "))
    #if statment incase user inputs an invalid grade
    if score < 0 or score > 100:
        print("INVALID score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{grade+1} again: "))
    #append score to grades list
    grades.append(score)
#print results
print("-"*13,"Results","-"*13)
#print lowest grade
print(f"Lowest Score  : {min(grades)}")
#remove lowest grade from grades list
grades.remove(min(grades))
#print new grades list
print(f"Modified List : {grades}")
#get average of grades list
avg = sum(grades) / len(grades)
#print average
print(f"Scores Average: {avg:.2f}")
#if statement to get letter grade
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    #print letter grade
print(f"Grade         : {letter_grade}")
print("-"*35)