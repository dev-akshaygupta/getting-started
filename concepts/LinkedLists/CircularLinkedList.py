### Circular Linked List ###

"""
Given a Linked List, the task is to insert a new node 
in this given Linked List at the following positions: 

- Insertion in an empty list
- At the front of the linked list
- At the end of the linked list.
- At a specific position.
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

def print_nodes(node):
	if node is None:
		return None

	# Start from the head node
	head = node.next
	while True:
		print(head.data, end=" ")
		head = head.next
		if head == node.next:
			break
	print()

# Insertion in an empty list
def insert_in_empty_list(last, data):
	new_node = Node(data)
	new_node.next = new_node
	return new_node

last = None
last = insert_in_empty_list(last, 1)
print("List after insertion: ", end="")
print_nodes(last)
print()

# At the front of the linked list
def insert_at_front(last, data):
	new_node = Node(data)

	# If the list is empty, initialize, it with the new node
	if last is None:
		new_node.next = new_node
		return new_node

	new_node.next = last.next
	last.next = new_node

	return last

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
third.next = first

print("Before insertion: ", end="")
print_nodes(third)
new_head = insert_at_front(third, 7)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# At the front of the linked list
def insert_at_end(last, data):
	new_node = Node(data)

	# If the list is empty, initialize, it with the new node
	if last is None:
		last = new_node
		new_node.next = new_node
		return last

	new_node.next = last.next
	last.next = new_node
	last = new_node

	return last

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
third.next = first

print("Before insertion: ", end="")
print_nodes(third)
new_head = insert_at_end(third, 7)
print("After insertion: ", end="")
print_nodes(new_head)
print()

# At a specific position.
def at_specified_position(last, pos, data):
	new_node = Node(data)

	if last is None:
		if pos != 1:
			print("Invalid position!")
			return last
		last = new_node
		last.next = last
		return last

	curr = last

	# Insert at the beginning
	if pos == 1:
		new_node.next = curr.next
		last.next = new_node
		return last

	# Traverse the list to find the insertion point
	while curr and pos > 1:
		# If position is out of bounds
		if curr.next.data == last.data:
			print("Position out of bounds")
			return
		curr = curr.next
		pos -= 1

	# Insert the new node at the desired position
	new_node.next = curr.next
	curr.next = new_node

	# Update last if the new node is inserted at the end
	if curr == last:
		last = new_node

	return last


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
third.next = first

print("Before insertion: ", end="")
print_nodes(third)
new_head = at_specified_position(third, 3, 7)
print("After insertion: ", end="")
print_nodes(new_head)
print()


"""
Delete a Circular Linked List node at a given position

- At the beginning
- At specified posn
- At the end
"""

# At the beginning
def delete_first_node(head):
	prev = head
	nxt = head
	if head is None or prev.next is nxt:
		return

	while prev.next != head:
		prev = prev.next
		nxt = prev.next

	prev.next = nxt.next

	head = prev
	return head


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
third.next = first

print("Before deletion: ", end="")
print_nodes(third)
new_head = delete_first_node(first)
print("After deletion: ", end="")
print_nodes(new_head)
print()


# At specified posn
def delete_at_specified_posn(head, posn):
	if head is None:
		print("List is empty")
		return

	temp = head

	# Delete head node
	if posn == 1:
		if head.next == head:		# Single node case
			return

		while temp.next != head:	# Find last node
			temp = temp.next

		head = head.next 			# Move head
		temp.next = head 			# Update last node's next pointer
		return

	prev = None
	for _ in range(posn - 1):
		prev, temp = temp, temp.next
		if temp == head:			# Out of bounds
			print("Invalid position")
			return

	prev.next = temp.next  # Unlink node
	return

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
third.next = first

print("Before deletion: ", end="")
print_nodes(third)
delete_at_specified_posn(first, 2)
print("After deletion: ", end="")
print_nodes(third)
print()


class Node:
	def __init__(self, value = None):
		self.value = value
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		
	def __iter__(self):
		node = self.head
		while node:
			yield node
			if node.next == self.head:
				break
			node = node.next
	
	# Create circular linked list
	def create_cirular_single_linked_list(self, value):
		new_node = Node(value)
		new_node.next = new_node
		self.head = new_node
		self.tail = new_node
		return "cirular_single_linked_list has been created."
	
	def insert_cirular_single_linked_list(self, value, loc):
		if self.head is None:
			return "Head reference is None."
		else:
			new_node = Node(value)
			if loc == 0:
				new_node.next = self.head
				self.head = new_node
				self.tail.next = new_node
			elif loc == 1:
				new_node.next = self.tail.next
				self.tail.next = new_node
				self.tail = new_node
			else:
				temp_node = self.head
				idx = 0
				while idx < loc - 1:
					temp_node = temp_node.next
					idx += 1
				new_node = temp_node.next
				temp_node.next = new_node
				new_node.next = new_node
		return "cirular_single_linked_list has been inserted."
	
	def traversal_cirular_single_linked_list(self):
		if self.head is None:
			return "Head reference is None."
		else:
			temp_node = self.head
			while temp_node:
				print(temp_node.value)
				temp_node = temp_node.next
				if temp_node == self.tail.next:
					break

	def search_cirular_single_linked_list(self, value):
		if self.head is None:
			return "Head reference is None."
		else:
			temp_node = self.head
			while temp_node:
				if temp_node.value == value:
					return temp_node
				temp_node = temp_node.next
				if temp_node == self.tail.next:
					return "Node does not exits"
				
	def delete_cirular_single_linked_list(self, loc):
		if self.head is None:
			return "Head reference is None."
		else:
			if loc == 0:
				if self.head == self.tail:
					self.head.next = None
					self.head = None
					self.tail = None
				else:
					self.head = self.head.next
					self.tail.next = self.head
			elif loc == 1:
				if self.head == self.tail:
					self.head.next = None
					self.head = None
					self.tail = None
				else:
					temp_node = self.head
					while temp_node:
						if temp_node.next == self.tail:
							break
						temp_node = temp_node.next
					temp_node.next = self.head
					self.tail = temp_node
			else:
				temp_node = self.head
				idx = 0
				while idx < loc - 1:
					temp_node = temp_node.next
					idx += 1
				next_node = temp_node.next
				temp_node.next = next_node.next
		
	def delete_entier_cirular_single_linked_list(self):
		self.head = None
		self.tail.next = None
		self.tail = None
	
# csll = CircularLinkedList()
# csll.create_cirular_single_linked_list(10)
# csll.insert_cirular_single_linked_list(20, 1)
# csll.insert_cirular_single_linked_list(30, 0)
# csll.insert_cirular_single_linked_list(40, 1)
# csll.insert_cirular_single_linked_list(50, 0)

# for obj in csll:
# 	print(obj.value)

# csll.traversal_cirular_single_linked_list()
# print(csll.search_cirular_single_linked_list(20))
# print(csll.delete_cirular_single_linked_list(2))
# csll.traversal_cirular_single_linked_list()
# print(csll.delete_entier_cirular_single_linked_list())
# csll.traversal_cirular_single_linked_list()