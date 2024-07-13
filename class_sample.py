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


class Addition:
    def twonumadd(num1,num2):
        return num1+num2

#Addition.twonumadd=staticmethod(Addition.twonumadd)    
#x=Addition() #if we use self in function then we need to create an instance 
#sum=x.twonumadd(10,20)
sum=Addition.twonumadd(10,20)
print(sum)