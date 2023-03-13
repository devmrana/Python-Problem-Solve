class Car():
	"""docstring for Country"""
	def __init__(self, n,c):
		self.name = n
		self.color = c

	def start(self):
		print("Name of the car: ",self.name)
		print("Car color: ",self.color)
		print("Starting the engine**")

myCar = Car("Corolla","Black")
myCar.start()
print("\n")
# new object myCar1
myCar1 = Car("Premio","Yellow")
Car.start(myCar1)
print("\n")
myCar1.year = "2021. (Year is the new Attribiute)"
print("\t>>>>",myCar1.name, myCar1.color, myCar1.year)
