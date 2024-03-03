class Transport_Vehicle:
    def __init__(self, name, maxspeed):
        self.name = name
        self.maxspeed = maxspeed
    def info(self):
        print(f"назва - {self.name} максимальна швидкість - {self.maxspeed}")
vehicle = Transport_Vehicle("автобус", "180")
vehicle.info()

