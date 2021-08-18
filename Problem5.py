class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


School = Bus("School Volvo", 180, 12)
print(School.color, School.name, School.max_speed, School.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, car.max_speed, car.mileage)