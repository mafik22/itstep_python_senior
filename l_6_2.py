class plane:
    def __init__(self, name, maxspeed, flight):
        self.name = name
        self.maxspeed = maxspeed
        self.flight = flight
    def info(self):
        print(f"назва - {self.name} максимальна швидкість - {self.maxspeed} дальність польоту - {self.flight}")
vehicle = plane("Літак", "2400", "17500")
vehicle.info()