class Vehicle():
    """Base class for all vehicle"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving >>> ", self.manufacturer, self.name, self.color)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stoping!")

# Car class is child-class


class Car(Vehicle):
    def change_gear(self, gear_name):
        print(self.name, "is changing gear to", gear_name)


# if __name__ == "__main__":
v1 = Car("Fusion", "Walton", "Black")

v1.brake()
v1.drive()
v1.turn("left")
v1.change_gear("P")
