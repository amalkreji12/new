class RacingTeamMembers:
    year=2024  #this year is for whole class
    def __init__(self,name,age,place):   #--> constructor
        self.name=name
        self.age=age
        self.place=place
        
    def addAge(self):
        self.age=self.age+1


    def relocate(self,place):
        self.place=place

    def displayAll(self):
        print('Name :',self.name)
        print('Age :',self.age)
        print('Place :',self.place)
        print('Year :',RacingTeamMembers.year)

    @classmethod                   # classmethod is used for class variable ie year.
    def changeYear(cls):
        cls.year=cls.year+1


    @staticmethod   #static method
    def display_welcome():
        print('Welcome')


x=RacingTeamMembers('bmw',1,'Germany')
y=RacingTeamMembers('audi',1,'France')

RacingTeamMembers.display_welcome()
x.displayAll()
y.displayAll()

print('--------Afer Update---------------')

RacingTeamMembers.changeYear()
x.addAge()
y.addAge()
x.relocate('USA')
y.relocate('UK')
x.displayAll()
y.displayAll()