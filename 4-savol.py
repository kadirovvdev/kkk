class Car:
    def __init__(self, name, make, year):
        self.__name = name
        self._make = make
        self.year = year


class Petrol_car(Car):
    def __init__(self, name, make, year, type_petrol, km):
        Car.__init__(self, name, make, year)
        self.type_petrol = type_petrol
        self.km = km

class Elektro_car(Car):
    def __init__(self, name, make, year, time_elektro, speed):

        Car.__init__(self, name, make, year)
        self.time_elektro = time_elektro
        self.speed = speed


class Hybrid_car(Petrol_car, Elektro_car):
    def __init__(self, name, make, year, type_petrol, km, time_elektro, speed, model, bak_hajm):

        Petrol_car.__init__(self, name, make, year, type_petrol, km)
        Elektro_car.__init__(self, name, make, year, time_elektro, speed)
        self.__model = model
        self.bak_hajm = bak_hajm

    def get_info(self):
        return f"Model:{self.__model}\nMake:{self._make}\nType_petrol:{self.type_petrol}\nKm:{self.km}\nTime_elektro:{self.time_elektro}\nSpeed:{self.speed}\nBak_hajm:{self.bak_hajm}"


car = Hybrid_car("BMW X5", "BMW","2023", "91+", "500km", "5 hours", "300 km/h", "New", "40 little")

print(car.get_info())