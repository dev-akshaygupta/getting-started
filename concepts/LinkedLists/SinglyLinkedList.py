### Singly Linked List ###

"""
Given a Linked List, the task is to insert a new node 
in this given Linked List at the following positions: 

- At the front of the linked list  
- Before a given node.
- After a given node.
- At a specific position.
- At the end of the linked list.
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# At the front of the linked list
def insert_at_front(head, data):
	new_node = Node(data)
	new_node.next = head
	return new_node

def print_nodes(node):
	if node is None:
		return None

	while node is not None:
		print(node.data, end=" ")
		node = node.next
	print()


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

print("Before insertion: ", end="")
print_nodes(first)
new_head = insert_at_front(first, 0)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# Before a given node.
# We identify the given node with provided key value.
def before_given_node(head, key, data):
	new_node = Node(data)

	# If the linked list is initially empty
	if head is None:
		return None

	# If key is found at the head node
	if head.data == key:
		new_node.next = head
		return new_node

	# Traverse the list to find the node wtih given key value
	prev = None
	curr = head
	while curr and curr.data != key:
		prev = curr
		curr = curr.next

	# If curr is not None add new node
	if curr:
		prev.next = new_node
		new_node.next = curr

	return head
	

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Before insertion: ", end="")
print_nodes(first)
new_head = before_given_node(first, 5, 10)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# After a given node.
# We identify the given node with provided key value.
def after_given_node(head, key, data):
	new_node = Node(data)

	# Traverse the list and find key node
	curr = head
	while curr is not None:
		if curr.data == key:
			break
		curr = curr.next

	# If key node not found
	if curr is None:
		return head

	# Add new node
	new_node.next = curr.next
	curr.next = new_node

	return head


first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Before insertion: ", end="")
print_nodes(first)
new_head = after_given_node(first, 3, 10)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# At a specific position.
# We identify the given node with position value
def after_given_node(head, pos, data):
	new_node = Node(data)

	# If node need to be inserted at first position
	if pos == 1:
		new_node.next = head
		return new_node

	# Traverse the list to find the given position
	curr = head
	for _ in range(1, pos-1):
		if curr == None:
			break
		curr = curr.next

	# If given position is outside the range of the list
	if curr is None:
		print("Position is out of bounds.")
		return head

	# Add new node at given position
	new_node.next = curr.next
	curr.next = new_node

	return head

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Before insertion: ", end="")
print_nodes(first)
new_head = after_given_node(first, 3, 10)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# At the end of the linked list.
def insert_at_end(head, data):
	new_node = Node(data)

	# If the linked list is initially empty
	if head is None:
		return None

	# Traverse to the last node
	last = head
	while last.next:
		last = last.next

	# Add new node
	last.next = new_node

	return head

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Before insertion: ", end="")
print_nodes(first)
new_head = insert_at_end(first, 10)
print("After insertion: ", end="")
print_nodes(new_head)
print()