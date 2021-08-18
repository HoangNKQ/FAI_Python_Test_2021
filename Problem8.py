class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_Bus = Bus(200, 3000)

print(isinstance(School_Bus, Vehicle))