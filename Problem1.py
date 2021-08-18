class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

#Class Test
car = Vehicle(100, 2000)
print(car.max_speed, car.mileage)

