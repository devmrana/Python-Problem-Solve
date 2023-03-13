class Car():
	"""docstring for Car"""
	name = ""
	color = ""

	def start():
		print("Starting the engine*")
Car.name = "Axio"
Car.color = "White"
print("Name of the car: ",Car.name)
print("Car color: ",Car.color)
Car.start()