#Multple Inheritance

class First:
    def display_first(self):
        print('First')

class Second(First): #multi level inheritance
    def display_second(self):
        print('Second')


class Third(Second):                                #left-right
    def display_third(self):
        print('Third')



x=Third()
x.display_first()
x.display_second()


 
###################################################################################

class First:
    def display_first(self):
        print('First')

class Second:                                   #Here in class second and third class function 'display' is same ,it is decided in left-right way                                                        
    def display(self):
        print('Second')


class Third(First,Second):                                #left-right
    def display(self):
        print('Third')

x=Third()
x.display()
print(Third.mro())  #mro will return the deciding order of classes