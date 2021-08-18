class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self):
        return super().seating_capacity(capacity = 50)

car = Vehicle("oto", 100, 2000)
print(car.seating_capacity(60))

hanoiBus = Bus("xe buyt", 200, 3000)
print(hanoiBus.seating_capacity())
