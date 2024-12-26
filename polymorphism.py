mytuple = ("apple","pinaple","banana")
thisdict = {
    "fruit": mytuple,
    "color": "thisdict"
}

print(len(mytuple))
print(len(thisdict))

"""SECTION ANOTHER LEARN"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def move(self):
        print("Car is moving Drive", self.brand, self.model, self.year)


class Boat:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Boat is moving Swim", self.brand, self.model, self.year)

class Plane:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Plane is moving Fly", self.brand, self.model, self.year)

car1 = Car("Ford", "Mustang", 2010)
boat1 = Boat("Sailboats", "Yacht", 2000)
plane1 = Plane("Airbus", "A320", 2015)

for x in (car1, boat1, plane1):
    x.move()


"""SECTION ANOTHER LEARN"""
class Vehicle:
    def __init__(obj, brand, model, year):
        obj.brand = brand
        obj.model = model
        obj.year = year
    
    def move(obj):
        print("move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(obj):
        print("swimming!")

class Plane(Vehicle):
    def move(obj):
        print("flying!")

car1 = Car("Ford", "Mustang", 2010)
boat1 = Boat("Sailboats", "Yacht", 2000)
plane1 = Plane("Airbus", "A320", 2015)

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    print(x.year)
    x.move()