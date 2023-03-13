# Car main class
class Car:
	"""docstring for Car"""
	name = ""
	color = ""
	#def start():
	def start(self):	#python suggest>(self) #write anythin like> m/main/etc..
		print("Starting the engine**")
# creating a Car object
myCar = Car()
myCar.name = "Allion"
myCar.color = "Black"
print("Name of the car: ",myCar.name)
print("Car color: ",myCar.color)
myCar.start()