



def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


print('Hi Welcome')
print('Operations')
print('1.Calculator\n2.Multiplication Table')
op=int(input('Select option...'))

if op==1:

    menu='Y' or 'y'
    while(menu=='Y' or menu=='y'):

        men='Y' or 'y'
        while(men=='Y' or men=='y'):
            print('Menu')
            print('1.Addition\n2.Substractions\n3.Multiplication\n4.Division')
            n=int(input('Choose operation to perform :'))
            if n==1:
                print('You have choosed Addition')
                break
            elif n==2:
                print('You have choosed Substraction')
                break
            elif n==3:
                print('You have choosed Multiplication')
                break
            elif n==4:
                print('You have choosed Division')
                break
            else:
                print("Invalid Input")
                men=input('Do you want to restart ? (Y/N)')
                if men=='N' or men=='n':
                    break
        if men=='N' or men=='n':
            break
    if men=='N' or men=='n':
        break
            

    a=int(input('Enter first number :'))
    b=int(input('Enter second number :'))

    if n==1:
        print('Answer is :',add(a,b))
    elif n==2:
        print('Answer is :',sub(a,b))
    elif n==3:
        print('Answer is :',mul(a,b))
    elif n==4:
        print('Answer is :',div(a,b))
    menu = input('Do you want to contion ? (Y/N)')
    if menu == 'N' or menu == 'n':
        break
    if menu == 'N' or menu == 'n':
        break
