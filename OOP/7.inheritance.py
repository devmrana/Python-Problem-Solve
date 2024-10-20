class Vehicle():
    """Base class for all vehicle"""

    def __init__(selfm, name, manufacturer, color, year):
        selfm.name = name
        selfm.manufacturer = manufacturer
        selfm.color = color
        selfm.year = year

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
# ----------------------------------------------------------------------

class Dancer:
    def __init__(self, style):
        self.style = style

    def dance(self):
        print(f'Dancing in {self.style}')


class Singer:
    def __init__(self, genre):
        self.genre = genre

    def sing(self):
        print(f'Singing {self.genre} music')


class Artist:
    def __init__(self, painting_material):
        self.painting_material = painting_material

    def paint(self):
        print(f'Painting with {self.painting_material}')


class SuperHuman(Dancer, Singer, Artist):
    def __init__(self, style, genre, paint_materials, sport):
        Dancer.__init__(self, style)
        Singer.__init__(self, genre)
        Artist.__init__(self, paint_materials)
        self.sport = sport

    def play_sport(self):
        print(f'Playing {self.sport}')

    # Overriding the Dance method of Dancer class
    def dance(self, competition="Fresher's Cup"):
        print(f'Dancing with my own {self.style} in the competition {competition}')


s_human = SuperHuman('Hip-Hop', 'Classical', 'Acrylic', 'Football')
# print(s_human.style)
# print(s_human.genre)
print(s_human.painting_material)
# print(s_human.sport)
s_human.dance()
s_human.sing()
# s_human.paint()
s_human.play_sport()

# print(help(SuperHuman))


