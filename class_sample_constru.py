class RacingTeamMenmers:
    year=2024
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
        print('Year :',RacingTeamMenmers.year)


x=RacingTeamMenmers('bmw',1,'Germany')
x.displayAll()


RacingTeamMenmers.year=RacingTeamMenmers.year+1
x.addAge()
x.displayAll()