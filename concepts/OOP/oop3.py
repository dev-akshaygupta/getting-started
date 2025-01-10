import csv

class Item:
	# Class attribute
	pay_rate = 0.8		# Discount offered on the product
	all = []

	# Constructor - magic method - called automatically
	def __init__(self, name: str, price: float, quantity=0):
		# Run validation for inputs
		assert price >= 0, f"Price {price} not greater than 0"
		assert quantity >= 0, f"Qauntity {quantity} not greater than 0"

		# Instance attributes
		self.name = name
		self.price = price
		self.quantity = quantity

		# Actions to execute
		Item.all.append(self)

	# Representation of the object - magic method - called automatically
	def __repr__(self):
		return f"Item ('{self.name}', '{self.price}', '{self.quantity}')"

	# Class method (will not be part of any instance)
	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)	# Converting to list
		
		for item in items:
			Item(name = item.get("name"), price = float(item.get("price")), quantity = int(item.get("quantity")))

	@staticmethod
	def is_integer(num):
		# We will count the floats that are point zero
		# For ex- 5.0, 10.0
		if isinstance(num, float):
			# Count the floats that are point zero
			return num.is_integer()
		elif isinstance(num, int):
			return True
		else:
			return False


	# User defined method - Instance method
	def calculate_total_price(self):
		return self.price * self.quantity

	# User defined method - Instance method
	def apply_discount(self):
		self.price = self.price * self.pay_rate	# pay_rate can be accessible using class name or self(instance level)

# Example3 - 
# Item.instantiate_from_csv()
# print(Item.all)
print(Item.is_integer(10.005))