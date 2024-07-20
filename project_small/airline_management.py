class Aircraft:
    def __init__(self,registration,model,capacity):
        self.registation=registration
        self.model=model
        self.capacity=capacity

    def __str__(self):
        return f'Registration:{self.registation},Model:{self.model},Capacity:{self.capacity}'
    

class AirlineManagementSystem:
    def __init__(self):
        self.aircrafts=[]

    def addAircraft():
        registration=input('Enter registration number of aircraft :')
        model=input('Enter the model of the aircraft :')
        capacity=int(input('Enter the capacity of the aircraft :'))

        aircraft=Aircraft(registration,model,capacity)

        self.aircrafts.append(aircraft)

        print('Aircraft added successfully')

    def displayAircrafts(self):
        if not self.aircrafts:
            print('No aircraft available')
        else:
            for aircraft in self.aircrafts:
                print(aircraft)
