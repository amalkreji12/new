# #Multiplication Table

# print('Hi Welcome')

# menu='Y'or'y'
# while(menu=='Y'or menu=='y'):

#     n=int(input('Enter number to print table :'))
#     print('You have choosed',n)

#     for i in range(1,11):
#         print(i,'x',n,':',i*n)

#     menu=input('Do you want to continue (Y/N)')
#     if menu == 'N' or menu=='n':
#         break



# Calculation

#Fuctions for calculations
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


print('Hi Welcome')
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