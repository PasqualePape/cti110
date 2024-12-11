#Pasquale Pape
#10/30/2024
#P4LAB2
#Use a for loop and a while loop to display positive mutiplication tables


#create a variable to make program run the first time
run_again = "yes"

#while loop to control entire program
while run_again == "yes":
    #get input from user
    user_num = int(input("Enter an integer: "))
    print()
    #check if user_num is positive
    if user_num >= 0:
        #loop to print the multiplication
        for num in range(1,13):
            print(f"{user_num} * {num} = {user_num*num}")
            
       #if user num is negative tell the user
    else:
        print("program does not handle negative numbers!!")
    print()
    run_again = input("would you like to run the program again (yes/no)? ").lower()
    print()
#loop breaks
print("Exiting program...")























