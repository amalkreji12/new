class BaseClass:
    def display(self):
        print('Hello')


class SubClass(BaseClass):
    def welcome(self):
        print('Welcome')

x=BaseClass()
x.display()

y=SubClass()
y.display()
y.welcome()