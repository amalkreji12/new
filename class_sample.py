class MySampleClass:
    def hello(self,n):
        self.name=n

    def print_name(self):
        print(self.name)


x=MySampleClass()
namee='apple'
x.hello(namee)
x.print_name()

y=MySampleClass()
y.hello('orange')
y.print_name()