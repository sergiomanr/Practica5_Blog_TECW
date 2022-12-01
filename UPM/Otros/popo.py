class Dog:
    """May god forgive ya"""
    def __init__(self,name: str,age: float):
        self.names = name #lo que va después de el self.___ es lo que fuera se llama
        self.age = age
    def sit(self):
        print(self.names,"is now siting")
    def roll_over(self):
        print(self.names,"is too old to roll over because he is",self.age)
# my_dog = Dog("Jerry",27)
# dog2 = Dog("Amanda",12)
# print("My dawg name is",my_dog.names.capitalize())s
# my_dog.roll_over()
# dog2.sit()


class Restaurant:
    def __init__(self,name,type):
        self.numer_seved = 5
        self.name = name
        self.type = type
    def describe_rest(self):
        print("The restaurant selected is called",self.name,"and serves",self.type,"food")
    def open_rest(self):
        print("The restaurant",self.name,"is open")
    def read_served(self):
        print("this has served",self.numer_seved,"people")
    def set_number_served(self,num:int):
        self.numer_seved = num
    def increment_number_served(self,incr: int):
        self.numer_seved += incr
    # def set_number_served(self):
class IceCreamStand(Restaurant):
    def __init__(self, name, type,):
        super().__init__(name, type)
        self.sabores = ["piña","jamon","platano"]
    
    def get_flavours(self):
        for i in self.sabores:
            print(i)

restaurant = Restaurant("pepis","edible")
Vips = Restaurant("Vips","mexican")
Popis = Restaurant("Popis","turkish")
telepizza = Restaurant("Telepizza","Italian")
restaurant2 = IceCreamStand("papas","icy",)
# restaurant.read_served()
# restaurant.numer_seved = 20 #cambiar desde fuera
# restaurant.set_number_served(35)    #cambiar por funcion
# restaurant.increment_number_served(12) 
# restaurant.read_served()
'''restaurant2.get_flavours()'''
class Admin:
    def __init__(self) -> None:
        self.privileges = Privileges()
class Privileges:
    privileges_list = ['can be gay','above law','can commit arson']
    def __init__(self,privileges=privileges_list) -> None:
        self.privileges = privileges
    def show_privileges(self):
            for i in self.privileges:
                print(i)
class User(Admin):
    def __init__(self,f_name: str,l_name:str,height: float ,age: int) -> None:
        self.first = f_name
        self.last = l_name
        self.height = height
        self.age = age
    def describe_user(self):
        print("The user's name is",self.first,self.last,"he is",self.height,"meters tall and is",self.age,"years old")
    def greet_user(self):
        print("Good morning",self.first,self.last)

jorge = User("Jorge","Pérez",1.86,22)
maria = User("María","gonzalez",1.53,56)

jefe = Admin()
jefe.privileges.show_privileges()
# jorge.describe_user()
# jorge.greet_user()

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print("This car has",self.odometer_reading,"miles on it")
    def update_odometer(self,mileage: float):
        if mileage >= self.odometer_reading:        #si lo que tiene es más o igual que lo previamente establecido hace lo nuevo lo que
            self.odometer_reading = mileage         # responde si no devuelve el mensaje y da lo prev establecido
        else:
            print("No podes cambier la verga esa puto")
    def incrment_odometer(self,miles):
        self.odometer_reading += miles              #coje lo nuevo o prev establecido y le mete un valor nuevo

class GordoCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def say_battery(self):
        print("My size of popo is",self.battery,"kWh bich")      #si en la de arriba solo está el self y al llamar a funcion no se pone nada este devuelve el tamaño puesto =

class Battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a",self.battery_size,"kWh battery")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print("the range is",range)
    


my_batmobiol = GordoCar("tesla","modelo gay",1492)
my_batmobiol.say_battery()
'''     
my_batmobiol.battery.describe_battery()             #cogemos el objeto en si, le metemos en la clase battery y luego ejecuta lo que se le pida
print(my_batmobiol.get_descriptive_name())
my_batmobiol.battery.get_range()'''
# my_batmobiol.say_battery(20)        
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# """my_new_car.odometer_reading = 23 # Una forma de cambiar el valor creado"""
# my_new_car.update_odometer(40)
# my_new_car.incrment_odometer(29)
# my_new_car.read_odometer()

