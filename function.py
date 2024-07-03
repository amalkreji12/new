def hey():
    print('Hello World')

hey()

def add(a,b):
    print(a+b)

add(3,3)

def name(n,age):
    print('Name is '+n+'and age is '+str(age))

name('Hello','12')

val='world'
name(val,12)


#function arbitary arguments

def arb(*values):
    print('First :',values[0],'Second :',values[1], 'Third :' ,(values[2]))

arb(1,2,3)


# Global and Local variables
num=10
def glo():
    num='hello'
    print(num)

glo()