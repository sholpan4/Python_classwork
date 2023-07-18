

class House:
    def __init__(self, floors, color, rooms, bathrooms):
        self.floors = floors
        self.color = color
        self.rooms = rooms
        self.bathrooms = bathrooms

    def get_info(self):
        info = "Дом %d-этажный, цвета %s, комнат: %d, ванных: %d" % \
               (self.floors, self.color, self.rooms, self.bathrooms)
        return info

my_house = House(2, "красный", 6, 2)
print(my_house.get_info())