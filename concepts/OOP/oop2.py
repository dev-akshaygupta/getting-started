class Item:
	# Class attribute
	pay_rate = 0.8		# Discount offered on the product
	all = []

	# Constructor
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

	# User defined method
	def calculate_total_price(self):
		return self.price * self.quantity

	# User defined method
	def apply_discount(self):
		self.price = self.price * self.pay_rate	# pay_rate can be accessible using class name or self(instance level)

	def __repr__(self):
		return f"Item ('{self.name}', '{self.price}', '{self.quantity}')"

# Example2 - 
item1 = Item("Phone", 100, 2)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Mouse", 50, 6)
item4 = Item("Keyboard", 60, 4)
item5 = Item("Cable", 25, 10)

print(Item.all)

for instance in Item.all:
	print(instance.name, instance.quantity)