''' 
Class --> Entity (Blueprint of Object)

Example:
Studnet --> Entity
Std_id, Course, Address are  --> Attributes.

'''

# class Car:
#     def __init__(self, tyres, doors, windows, engine_type):
#         self.tyres = tyres
#         self.doors = doors
#         self.window = windows
#         self.engine_type = engine_type
    
#     def drive(self):
#         print(f"The type of car is {self.engine_type}")

# if __name__ == "__main__":
#     car_01 = Car(4,2,2,"Petrol")
#     # car_02 = Car()

#     # car_01.tyres = 4
#     # car_02.tyres = 4

#     car_01.drive()
#     # print(dir(car_02.tyres)) == dir is use to check the inside pre define method




# class Animal:
#     def __int__(self,*args):
#         if len(args) == 1:
#             self.name = args[0]
#         elif len(args) == 2:
#             self.name = args[0]
#             self.species = args[1]
#         elif len(args) == 3:
#             self.name = args[0]
#             self.species = args[1]
#             self.age = args[3]
        
#     def walk(self):
#         print(f"{self.name} is walking")



# if __name__ == "__main__":
#     deer = Animal("Deer", "Domestic")
#     deer.walk()



# creating class naming "vehicles"
class Vehicle:
    def __init__(self, brand, model): # self is connection between object and class attributes
        self.brand = brand
        self.model = model

    #creating new Method on same class
    def detail(self):
        return f'{self.brand} {self.model}'
    
#creating child class
class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_Byd = ElectricCar("BYD","BT5","80kwh")
print(my_Byd.detail())

#creating object of Vehicles naming my_car
# my_car = Vehicle("Toyota","Fortuner")  

# print(my_car.brand)  #'''accessing the class attributes through object'''
# print(my_car.model)

# print(my_car.detail())



