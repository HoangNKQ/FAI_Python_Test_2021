class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

hanoiBus = Bus(200, 3000)
print(hanoiBus.max_speed, hanoiBus.mileage)