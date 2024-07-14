class BaseClass:
    def __init__(self):
        print('Base init')

    def set_name(self, name):
        self.name=name
        print('Base class set_name')


class SubClass(BaseClass): 
    def __init__(self):
        super().__init__()  #super() is used to call from baseclass  (over riding concept)
        print('Sub class init')

    def set_name(self, name):
        super().set_name(name)
        #self.name=name
        print('Sub class set_name')

    def welcome(self):
        print('Welcome')

    def display_name(self):
        print(self.name)

y=SubClass()
y.welcome()
y.set_name('Apple')
y.display_name()