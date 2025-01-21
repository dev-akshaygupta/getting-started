### Types of LinkedLists ###

# 1. Singly Linked List
# first -> second -> third -> fourth -> None
# (1, ptr2) -> (2, ptr3) -> (3, ptr4) -> (4, None)

# Definition of a Node in a Singly linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def print_nodes(node):

	# Iterate till node reaches None
	while node is not None:
		print(node.data, end=" ")
		node = node.next
	print()

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

first.next = second
second.next = third
third.next = fourth

print("Singly linked list: ", end="")
print_nodes(first)
print()

# 2. Doubly Linked List
# None <-> first <-> second <-> third <-> fourth <-> None
# (None, 1, ptr2) <-> (ptr1, 2, ptr3) <-> (ptr2, 3, ptr4) <-> (ptr3, 4, None) <-> None

# Definition of a Node in a Doubly linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

def print_nodes_Left_to_Right(node):
	
	# Iterate till node reaches None
	while node is not None:
		print(node.data, end=" ")
		node = node.next
	print()


def print_nodes_Right_to_Left(node):

	# Iterate till node reaches None
	while node is not None:
		print(node.data, end=" ")
		node = node.prev
	print()

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

second.prev = first
third.prev = second
fourth.prev = third

first.next = second
second.next = third
third.next = fourth

print("Doubly linked list")
print("Left to right: ", end="")
print_nodes_Left_to_Right(first)
print("Right to left: ", end="")
print_nodes_Right_to_Left(fourth)
print()

# 3. Circular Linked List
# first -> second -> third -> fourth -> first
# (1, ptr2) -> (2, ptr3) -> (3, ptr4) -> (4, ptr1)
#	   ^_____________________________________^

# Definition of a Node in a Circular Linked List
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def print_nodes(node):
	if node is None:
		return None

	head = node.next
	
	# Iterate till node reaches None
	while True:
		print(head.data, end=" ")
		head = head.next
		if head == node.next:
			break
	print()

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

first.next = second
second.next = third
third.next = fourth
fourth.next = first

print("Circular Linked List: ", end="")
print_nodes(fourth)
print()

# 4. Doubly Circular Linked List
# first <-> second <-> third <-> fourth <-> first
# (ptr4, 1, ptr2) <-> (ptr1, 2, ptr3) <-> (ptr2, 3, ptr4) <-> (ptr3, 4, ptr1)

# Definition of a Node in a Circular Linked List
class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

def print_nodes_Left_to_Right(node):
	if node is None:
		return None

	head = node
	
	# Iterate till node reaches None
	while True:
		print(head.data, end=" ")
		head = head.next
		if head == node:
			break
	print()


def print_nodes_Right_to_Left(node):
	if node is None:
		return None

	head = node.prev
	
	# Iterate till node reaches None
	while True:
		print(head.data, end=" ")
		head = head.prev
		if head.next == node:
			break
	print()

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

first.prev = fourth
second.prev = first
third.prev = second
fourth.prev = third

first.next = second
second.next = third
third.next = fourth
fourth.next = first

print("Circular Linked List: ", end="")
print("Left to right: ", end="")
print_nodes_Left_to_Right(first)
print("Right to left: ", end="")
print_nodes_Right_to_Left(first)
print()