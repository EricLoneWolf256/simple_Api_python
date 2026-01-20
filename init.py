# class Car:
#     total_cars = 0
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         Car.total_cars += 1
        
#     def display_info(self):
#         print(f"Car: {self.make} {self.model} {self.year}")
        
#     @classmethod
#     def display_total_cars(cls):
#         print(f"Total cars: {cls.total_cars}")
        
# car1 = Car("Toyota", "Camry", 2020)
# car2 = Car("Honda", "Accord", 2018)
# car3 = Car("Dodge", "Mustage" ,2005)




# print(f"Car 1: {car1.make}, {car1.model}, {car1.year}")

# print(f"Car 2: {car2.make}, {car2.model}, {car2.year}")

# print(f"Car 3: {car3.make}, {car3.model}")

# car1.year = 2021
# print(f"Updated yearr of car 1: {car1.year}")

# car1.display_info()
# car2.display_info()
# car3.display_info()
# Car.display_total_cars()

from tkinter import Y

from numpy import add


class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
tot_sam = MathUtils.add(6,8)

print(tot_sam)