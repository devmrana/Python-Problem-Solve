class Car():
	"""docstring for Car"""
	name = ""
	color = ""

	def __init__(self, name,color):
		self.Carname = name
		self.Carcolor = color

	def start(self):
		print("Starting the engine*")
		
myCar = Car("Corolla","Yellow")
print(myCar.Carname)	#self.Carname = name
print(myCar.Carcolor)	#self.Carcolor = color
myCar.start()

