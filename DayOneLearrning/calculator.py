# Below is the code for a simple calculator. You have 2 main tasks here:
# 1. Edit the code to ensure that it calculates correctly
# 2. Add code to do an additional calculation

print("Welcome to this calculator app! Enter the operator you want to use by choosing the corresponding number... ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    operator = input("Enter operator option: ")

    if operator in ('1', '2', '3', '4'):
        firstnum = float(input("Enter first number: "))
        secondnum = float(input("Enter second number: "))

        if operator == '1':
            print(firstnum, "+", secondnum, "=", firstnum + secondnum)

        elif operator == '2':
            print(firstnum, "-", secondnum, "=", firstnum - secondnum)

        # read this block - is this correct? edit it to make sure it is
        elif operator == '3':
            print(firstnum, "x", secondnum, "=", firstnum x secondnum)

        elif operator == '4':
            print(firstnum, "/", secondnum, "=", firstnum / secondnum)

        # add an additional statement here to calculate the power of the first number by the second number
        # for example, firstnum is 2, secondnum is 4, so you will calculate 2 to the power of 4 
        # you will also need to edit the code above to add an additional option (5)
        # this means adding another print statement and an additional input option

        break
    else:
        print("Invalid Input")
