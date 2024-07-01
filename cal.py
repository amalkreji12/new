def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

def mul(num1,num2):
    return num1*num2


menu = 'Y' or 'y'
while (menu == 'Y' or menu == 'y'):
    print("Menu")
    print(" Press 1 for Addition\n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division")
    a = input("Enter your selection: ")
    b = int(input("Enter first number: "))
    c = int(input("Enter second number: "))
    if a == '1':
        d=add(b,c)
        print(d)
    elif a == '2':
        d = sub(b,c)
        print(d)
    elif a == '3':
        d = mul(b,c)
        print(d)
    elif a == '4':
        d = div(b,c)
        print(d)
    else:
        print("invalid input.")
    menu = input("Do you want to continue? (Y/N)")
    if menu == 'N'or menu == 'n':
        break