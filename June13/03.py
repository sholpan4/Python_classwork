class Kettle ():
    temperature = 20
    material = "" 
    color = "" 
    volume = 0 
    water = 0

    def __init__(self, material, color, volume):
        self.material = material
        self.color = color
        self.volume = volume

    def fill(self, liters): 
        self.water += liters
        if self.water > self.volume:
            print(f"{self.water - self.volume} liters are not fit to the kettle")
            self.water = self.volume

        print (f"Now in the kettle {self.water} l")

    def pour(self, liters):
        
        if liters > self.water:
            print(f"Can't pour more than {self.water} liters.")
            self.water = 0
            
        else:
            self.water -= liters
            print(f"Now ther is a {self.water} liters in the kettle.")

    def boil(self):
        self.temperature = 100
        print("wheee") 



my_kettle = Kettle("iron", "black", 3)
my_kettle.fill(5)
print(my_kettle.__init__)