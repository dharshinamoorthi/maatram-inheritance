

class bike:
    def __init__(self, color, CC, mileage, year_of_manufactured):
        self.color = color
        self.CC = CC
        self.mileage = mileage
        self.color = color
        self.year_of_manufactured = year_of_manufactured

    def engine(self):
        return f"The engine is {self.CC} CC"


class electric_vehicle:   
    def __init__(self, charging_time):
        self.charging_time = charging_time

    def charging(self):
        return f"It will take {self.charging_time} to charge the bike"


class yamaha(bike):
    def __init__(self, color, CC, mileage, year_of_manufactured, type_of_engine):
    
        super().__init__(color, CC, mileage, year_of_manufactured)
        self.type_of_engine = type_of_engine



class R15(yamaha):
    def __init__(self, color, CC, mileage, year_of_manufactured, type_of_engine, top_speed):
        super().__init__(color, CC, mileage, year_of_manufactured, type_of_engine)
        self.top_speed = top_speed

class ola(bike, electric_vehicle):
    def __init__(self, color, CC, mileage, year_of_manufactured, charging_time):
        bike.__init__(self, color, CC, mileage, year_of_manufactured)
        electric_vehicle.__init__(self, charging_time)

        



bike1 =ducati('red', 150, 40, 2019, '2 stroke')
bike1.engine()



bike2 = passion pro('black', 150, 40, 2020, '4 stroke', 200)
bike2.top_speed


bike3 = tvs('red', 100, 50, 2021, 5)
print(bike3.year_of_manufactured)