# Learning to use user defined functions 
#Define a multiply function
def multiply(num1, num2, num3):
    product = num1 * num2 * num3 
    print(product)

#Define an add function
def add(num1, num2, num3):
    result = num1 + num2 + num3 
    print(result)


#define the main function - all your logic goes here
def main():
    #get some input form the user

    first_num = int(input("gimme a number: "))
    second_num = int(input("gimme a number: "))
    third_num = int(input("gimme a number: "))
    #call the multiply function
    multiply(first_num, second_num, third_num)
    #call the add function
    add(first_num, second_num, third_num)
#call the mainfunction
if __name__ == "__main__":
    main()
    