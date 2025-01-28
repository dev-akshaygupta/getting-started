### Doubly Linked List ###

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
		self.prev = None
		self.next = None

def print_nodes(node):
	if node is None:
		return None

	while node is not None:
		print(node.data, end=" ")
		node = node.next
	print()

# At the front of the linked list
def insert_at_front(head, data):
	new_node = Node(data)

	new_node.next = head

	# Change prev of head node to new node
	if head is not None:
		head.prev = new_node

	return new_node


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.prev = first
second.next = third
third.prev = second

print("Before insertion: ", end="")
print_nodes(first)
new_head = insert_at_front(first, 4)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# Before a given node.
# We identify the given node with provided key value.
def before_given_node(head, key, data):
	curr = head

	new_node = Node(data)

	while curr:
		if curr.data == key:
			break
		curr = curr.next

	# If curr becomes None, the given key is not found in the linked list
	if curr is None:
		return head

	new_node.prev = curr.prev		# Set prev of new node to prev of given node
	new_node.next = curr			# Set next of new node to given node

	# Update next of given node's prev to new node
	if curr.prev is not None:
		curr.prev.next = new_node
	else:
		# If the current node is the head, update the head
		head = new_node

	# Update prev of given node to new node
	curr.prev = new_node

	return head


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.prev = first
second.next = third
third.prev = second

print("Before insertion: ", end="")
print_nodes(first)
new_head = before_given_node(first, 3, 5)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# After a given node.
# We identify the given node with provided key value.
def after_given_node(head, key, data):
	curr = head

	new_node = Node(data)

	while curr:
		if curr.data == key:
			break
		curr = curr.next

	# If curr becomes None, the given key is not found in the linked list
	if curr is None:
		return head

	new_node.prev = curr		# Set prev of new node to the given node
	new_node.next = curr.next	# Set next of new node to the next of the given node
	curr.next = new_node		# Update next of the given node to new node

	# Update the prev of new node's next with the new node
	if curr.next is not None:
		curr.next.prev = new_node

	return head


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.prev = first
second.next = third
third.prev = second

print("Before insertion: ", end="")
print_nodes(first)
new_head = after_given_node(first, 3, 5)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# At a specific position.
# We identify the given node with position value
def at_specified_position(head, pos, data):
	new_node = Node(data)

	# Insertion at the beginning
	if pos == 1:
		new_node.next = head

		if head:
			head.prev = new_nod

		head = new_node
		return head

	curr = head
	pos -= 2

	while pos > 0:
		if curr is None:
			print("Position is out of bounds.")
			return head
		curr = curr.next
		pos -= 1

	# If the position is out of bounds
	if curr is None:
		print("Position is out of bounds.")
		return head

	new_node.prev = curr		# Set the prev of new node to curr
	new_node.next = curr.next	# Set the next of new node to next of curr
	curr.next = new_node		# Update the next of current node to new node

	# If the new node is not the last node, update prev of next node to new node
	if new_node.next:
		new_node.next.prev = new_node

	return head


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.prev = first
second.next = third
third.prev = second

print("Before insertion: ", end="")
print_nodes(first)
new_head = at_specified_position(first, 4, 9)
print("After insertion: ", end="")
print_nodes(new_head)
print()


# At the end of the linked list.
def insert_at_end(head, data):
	new_node = Node(data)

	# If the linked list is empty, set the new node as the head
	if head is None:
		head = new_node
		return head
	else:
		curr = head
		while curr.next:
			curr = curr.next

		curr.next = new_node	# Set the next of the last node to the new node
		new_node.prev = curr	# Set the prev of the new node to the last node
	return head


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.prev = first
second.next = third
third.prev = second

print("Before insertion: ", end="")
print_nodes(first)
new_head = insert_at_end(first, 10)
print("After insertion: ", end="")
print_nodes(new_head)
print()


"""
Delete a Doubly Linked List node at a given position
"""

# At the end of the linked list.
def delete_at_sepcified_pos(head, pos):
	# If the list is empty
	if head is None:
		return head

	curr = head

	for i in range(1, pos):
		curr = curr.next

	if curr is None:
		return head

	# Update the next node's prev pointer
	if curr.prev is not None:
		curr.prev.next = curr.next

	# Update the next node's prev pointer
	if curr.next is not None:
		curr.next.prev = curr.prev

	# If the node to be deleted is the head node
	if head == curr:
		head = curr.next

	# Deallocate memory for the deleted node
	del curr
	return head


first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

first.next = second
second.prev = first
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth

print("Before deletion: ", end="")
print_nodes(first)
new_head = delete_at_sepcified_pos(first, 3)
print("After deletion: ", end="")
print_nodes(new_head)
print()

