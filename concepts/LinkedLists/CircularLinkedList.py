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
