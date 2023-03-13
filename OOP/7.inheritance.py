class Vehicle():
    """Base class for all vehicle"""

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year

    def drive(self):
        print("Driving >>> ", self.manufacturer, self.name, self.color)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stoping!")

        # Car class is child-class

class Car(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color, year)  # Method overridding close
        # self.year = "" # / 2021
        self.wheels = 4

        print("A new car has been created > Name: ", self.name)
        print("It has ", self.wheels, "wheels")
        print("The car was built in ", self.year)

    def Car_details(self):
        print(
            f'Car name: {self.name}, Company name: {self.manufacturer}, Color: {self.color}, Year: {self.year}, Total wheels: {self.wheels}')

# MotorCycle class is child-class
class MotorCycle(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        super().__init__(name, manufacturer, color, year)

        self.wheels = 2
        print("A MotorCycle insert database", self.name)
        print("It has", self.wheels, "wheels")
        print("MotorCycle was builts ", self.year)

    def MC_details(self):
        print(
            f'MotorCycle name: {self.name}, Company name: {self.manufacturer}, Color: {self.color}, Year: {self.year}, Total wheels: {self.wheels}')


if __name__ == "__main__":
    car = Car("Mustrang", "Ford", "Red", "2021")  # must empty year
    car.Car_details()
    """car.turn("Left")
	car.brake()
	car.drive()"""
    print("\n")

    mc = MotorCycle("R15 V3", "Harley-Davidson", "Black", "2020")
    mc.drive()
    print("\n")
    mc.MC_details()
