

class Vehicle:
    def __init__(self,make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type



class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)


class ElectricCar(Car):
    def __init__(self, make, model, year, fuel_type, battery_capacity):
        super().__init__(make, model, year, fuel_type)
        self.battery_capacity = battery_capacity

    def info(self):
        return f'{self.make}-{self.model}-{self.year}-{self.fuel_type}-{self.battery_capacity}'
    
my_BYD = ElectricCar('BYD','BT5','2022','electric','80kwh')
print(my_BYD.info())


class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)


class HyrbidTruck(Truck):
    def __init__(self, make, model, year, fuel_type, electric_motor_power):
        super().__init__(make, model, year, fuel_type)
        self.electric_moto_power = electric_motor_power

    def info(self):
        return f'{self.make}-{self.model}-{self.year}-{self.fuel_type}-{self.electric_moto_power}'


my_truck = HyrbidTruck('Benz','Monster','2019','Diesel','battery')
print(my_truck.info())