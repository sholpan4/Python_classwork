class Kettle ():
    material = "" #steel
    color = "" #red
    volume = 0 #2.4
    water = 0

    def __init__(self, material, color, volume):
        self.material = material
        self.color = color
        self.volume = volume

    def fill(self, liters): #SELF обязателен
        self.water += liters  #(+=)если просто равно оставить, то print(my_kettle.water) не будет прибавлять
        print(f"Now in the kettle {self.water} l")  #"Now in the kettle", self.water, "l"

    

# my_kettle = Kettle()
# other_kettle = Kettle()

# my_kettle.color = "blue"

# Kettle.color = "white" #не стоит менять своиство класса

# print(my_kettle.color, other_kettle.color)
# my_kettle.fill(2)
# my_kettle.fill(1)
# print(my_kettle.water)

my_kettle = Kettle("steel", "red", 2)
my_kettle.fill(3)

Kettle.color = "black"
print(my_kettle.color)