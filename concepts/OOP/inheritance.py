# Base class
class Vehical:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def display_info(self):
		return f"Brand: {self.brand}, Model: {self.model}"

# Derived class
class Cars(Vehical):
	def __init__(self, brand, model, doors):
		super().__init__(brand, model)			# Call to base class constructor
		self.doors = doors

	def display_info(self):
		# Extend the functionality of the base class method
		base_info = super().display_info()
		return f"{base_info}, Doors: {self.doors}"


# Derived class
class Motorcycle(Vehical):
	def __init__(self, brand, model, engine_type):
		super().__init__(brand, model)			# Call to base class constructor
		self.engine_type = engine_type

	def display_info(self):
		# Extend the functionality of the base class method
		base_info = super().display_info()
		return f"{base_info}, Engine type: {self.engine_type}"

# Using the derived classes
car = Cars("Toyota", "Camry", 4)
motorcycle = Motorcycle("Yamaha", "R1", "Inline-4")

print(car.display_info())  # Brand: Toyota, Model: Camry, Doors: 4
print(motorcycle.display_info())  # Brand: Yamaha, Model: R1, Engine Type: Inline-4