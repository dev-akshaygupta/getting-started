class Item:
	# Class attribute
	pay_rate = 0.8		# Discount offered on the product

	# Constructor
	def __init__(self, name: str, price: float, quantity=0):
		# Run validation for inputs
		assert price >= 0, f"Price {price} not greater than 0"
		assert quantity >= 0, f"Qauntity {quantity} not greater than 0"

		# Instance attributes
		self.name = name
		self.price = price
		self.quantity = quantity

	# User defined method
	def calculate_total_price(self):
		return self.price * self.quantity

	# User defined method
	def apply_discount(self):
		self.price = self.price * self.pay_rate	# pay_rate can be accessible using class name or self(instance level)

# Example1 - 
item1 = Item("Phone", 100, 2)
item2 = Item("Laptop", 1000, 3)

print(item1.name, item2.name)
print(item1.price, item2.price)
print(item1.quantity, item2.quantity)

print(Item.pay_rate)
print(item1.pay_rate)

print(Item.__dict__)	# All attributes associated to a class
print(item1.__dict__)	# All attributes associated to an instance

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.95
item2.apply_discount()
print(item2.price)