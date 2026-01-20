class Vehicle:
    def __init__(self, brands, wheels):
        self.brand = brands
        self.wheels = wheels

    def describe(self):
        print(f"This is a {self.brand} vehicle with {self.wheels } wheels.")

class Car(Vehicle):
    def __init__(self, brands, wheels, model):
        super().__init__(brands, wheels )
        self.model = model

    def describe(self):
        print(f"This is a {self.brand} {self.model}  car with {self.wheels} wheels ")

class Motorcycle(Vehicle):
    def __init__(self, brands, wheels, cc ):
        super().__init__(brands, wheels)
        self.cc = cc 

    def describe(self):
        print(f"This is a {self.brand} Motorcycle with {self.cc} cc engine and {self.wheels} wheels")

vehicle = Vehicle("Generic", 4)
car = Car("Toyata",4,"Corolla")
bike = Motorcycle("Yamaha",2, 150)

vehicle.describe()
car.describe()
bike.describe()