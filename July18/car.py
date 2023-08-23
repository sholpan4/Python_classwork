class Car:
    def __init__(self, model, speed, color, bak_max, consumption):
        self.model = model
        self.speed = speed
        self.color = color
        self.bak_max = bak_max
        self.consumption = consumption / 100
        self.fuel_volume = 5

    def refuel(self, liters):
        if self.fuel_volume + liters <= self.bak_max:
            self.fuel_volume += liters
            print("В баке:", self.fuel_volume, "л")
        else:
            over_fill = self.fuel_volume + liters - self.bak_max
            self.fuel_volume = self.bak_max
            print("Перелив:", over_fill, "л бак полный")

    def go(self, km):
        fuel_waste = self.consumption * km
        if self.fuel_volume >= fuel_waste:
            time = km / self.speed
            self.fuel_volume -= fuel_waste
            print(f'Мы приехали за {time} часов и в баке осталось {self.fuel_volume} л')
        else:
            print("На поездку надо", fuel_waste, "л. а в баке ", self.fuel_volume)

class PorsheCayenne(Car):
    def __init__(self, color):
        super().__init__('PorsheCayenne', 150, color, 60, 10)

class Lamborgini(Car):
    def __init__(self, color, extra_light):
        super().__init__('Lamborgini', 200, color, 50, 20)
        self.extra_light = extra_light

car = Car('Porshe', 150, 'black', 50, 10)
car.refuel(30)
car.go(80)

car = PorsheCayenne('yellow')
car.refuel(30)
car.go(80)

car = Lamborgini('red', 'green')
car.refuel(45)
car.go(250)