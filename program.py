print('Hi Welcome')


menu='Y'or'y'
while(menu=='Y'or menu=='y'):

    n=int(input('Enter number to print table :'))
    print('You have choosed',n)

    for i in range(1,11):
        print(i,'x',n,':',i*n)

    menu=input('Do you want to continue (Y/N)')
    if menu == 'N' or menu=='n':
        break
