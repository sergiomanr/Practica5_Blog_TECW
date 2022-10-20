class Vehicle:
    def __init__(self,name: str,max_speed: float,milage:float):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
        if self.name.startswith('Audi'):
            self.color = 'white'
        elif self.name.startswith('Mercedes'):
            self.color = 'black'
    def say_stats(self):
        msg = 'Vehicle name: ' + self.name + '\t' + 'Speed: ' + str(self.max_speed) + '\t' + 'Milage: '+str(self.milage)+'\t'+'Color: '+ self.color
        print(msg)
class Bus(Vehicle):
    def __init__(self,name:str,max_speed:float,milage:float):
        super().__init__(name,max_speed,milage)
    def seating_capacity(self,capacity= 50):
        print('The',self.name,'has',capacity,'aviable seats')
class Car(Bus):
    def __init__(self, name: str, max_speed: float, milage: float):
        super().__init__(name, max_speed, milage)
        self.type = 'sedan'
    def say_lolita(self):
        print('The type of car is',self.type)
            

volvo = Vehicle('Volvo school bus',180,12)
audi = Car('Audi q4',240,59)
mercedes = Bus('Mercedes One',350,500)
# print(isinstance(audi, Car))
audi.say_stats()
audi.say_lolita()
# print(type(Color()))
# volvo.say_stats()
# audi.seating_capacity()
# mercedes.say_stats()