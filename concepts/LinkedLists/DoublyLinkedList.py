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


"""
Given a doubly-linked list of positive integers. 
The task is to print the given doubly linked list data in reverse order.
"""

def print_in_reverse(head):
	curr = head

	while curr.next:
		curr = curr.next

	print("Reverse order: ", end="")

	while curr:
		print(curr.data, end=" ")
		curr = curr.prev

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

print("Actual order: ", end="")
print_nodes(first)
print_in_reverse(first)
print()


"""
Given a Doubly linked list(DLL) containing n nodes and an integer x, 
the task is to find the position of the integer x in the doubly linked list. 
If no such position found then print -1.
"""

def search_node(head, data):
	curr = head
	count = 1

	while curr.next:
		if curr.data == data:
			return count
		count += 1
		curr = curr.next

	return -1

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(7)
fifth = Node(5)

first.next = second
second.prev = first
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth

print()
print("Doubly linked list: ", end="")
print_nodes(first)
posn = search_node(first, 7)
print(f"Node found at: {posn}", end="")
print()
print()

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def __iter__(self):
		curr = self.head
		while curr:
			yield curr
			curr = curr.next

	def __str__(self):
		curr = self.head
		result = 'None <- '
		while curr:
			result += str(curr.value)
			if curr.next:
				result += ' <-> '
			curr = curr.next
		result += ' -> None'
		return result

	# create doubly linked list
	def create(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length += 1
		return "Doubly linkedlist is created successfully!"
	
	# insert into doubly linked list
	def insert(self, value, loc):
		if self.head is None:
			print("The node cannot be inserted.")
		else:
			new_node = Node(value)
			if loc == 0:				# Insert at the beginning
				new_node.next = self.head
				self.head.prev = new_node
				self.head = new_node
			elif loc == -1:				# Insert at the end
				new_node.prev = self.tail
				self.tail.next = new_node
				self.tail = new_node
			else:						# Insert in the middle
				curr = self.head
				idx = 0
				while idx < loc-1 and curr is not None:
					curr = curr.next
					idx += 1
				
				if curr is None or curr.next is None:
					new_node.prev = self.tail
					self.tail.next = new_node
					self.tail = new_node
				else:
					new_node.next = curr.next
					new_node.prev = curr
					new_node.next.prev = new_node
					curr.next = new_node
			self.length += 1

	def append(self, value):
		new_node = Node(value)
		if not self.head:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node
		self.length += 1
	
	def prepend(self, value):
		new_node = Node(value)
		if not self.head:
			self.head = new_node
			self.tail = new_node
		else:
			self.head.prev = new_node
			new_node.next = self.head
			self.head = new_node
		self.length += 1

	def traverse(self):
		if not self.head:
			print("No nodes available to traverse.")
		else:
			curr = self.head
			while curr:
				print(curr.value)
				curr = curr.next

	def reverse_traverse(self):
		if not self.head:
			print("No nodes available to traverse.")
		else:
			curr = self.tail
			while curr:
				print(curr.value)
				curr = curr.prev

	def search(self, value):
		if not self.head:
			return "No nodes available to search."
		else:
			curr = self.head
			while curr:
				if curr.value == value:
					return curr
				curr = curr.next
			return "Value node not found in the list."
		
	def set(self, idx, value):
		node = self.get(idx)
		if node:
			node.value = value
			return f"Value at {idx} has been successfully updated."
		return f"Index out of bounds"
		
	def get(self, idx):
		if idx < 0 or idx >= self.length:
			return None

		if idx < self.length//2:
			curr = self.head
			for _ in range(idx):
				curr = curr.next
		else:
			curr = self.tail
			for _ in range(self.length-1, idx, -1):
				curr = curr.prev
		return curr
	
	def pop_first(self):
		if not self.head:
			print("No node available to pop")
			return
		
		popped_node = self.head
		if self.length == 1:
			self.head = self.tail = None
		else:
			self.head = self.head.next
			self.head.prev = None
			popped_node.next = None
		self.length -= 1
		return popped_node
	
	def pop(self):
		if not self.head:
			print("No node available to pop")
			return
		
		popped_node = self.tail
		if self.length == 1:
			self.head = self.tail = None
		else:
			self.tail = self.tail.prev
			self.tail.next = None
			popped_node.prev = None
		self.length -= 1
		return popped_node
	
	def remove(self, idx):
		if idx == 0:
			return self.pop_first()
		
		if idx == self.length-1:
			return self.pop()

		popped_node = self.get(idx)
		if popped_node:
			popped_node.prev.next = popped_node.next
			popped_node.next.prev = popped_node.prev
			popped_node.next = None
			popped_node.prev = None
			self.length -= 1
			return f"Node has been successfully deleted"

		return f"Index out of bounds"


	def delete(self, loc):
		if not self.head:
			print("No node available to delete")
			return
		
		if self.head == self.tail:
			self.head = self.tail = None
		elif loc == 0:
			self.head = self.head.next
			self.head.prev = None
		elif loc == -1:
			self.tail = self.tail.prev
			self.tail.next = None
		else:
			curr = self.head.next
			idx = 0
			while curr is not None and idx < loc-1:
				curr = curr.next
				idx += 1
			
			if curr is None:
				print("Index out of bounds")
				return

			if curr == self.tail:
				self.tail = self.tail.prev
				self.tail.next = None
			else:
				curr.prev.next = curr.next
				curr.next.prev = curr.prev
		self.length -= 1

	def delete_DLL(self):
		if not self.head:
			print("There are no nodes in the Linked List")
		else:
			curr = self.head
			while curr:
				curr.prev = None
				curr = curr.next
			self.head = None
			self.tail = None
			print("DLL is successfully deleted.")
			self.length = 0

doublyLL = DoublyLinkedList()
doublyLL.create(10)
doublyLL.insert(-10, 0)
doublyLL.insert(30, -1)
doublyLL.insert(20, 2)
print([node.value for node in doublyLL])
doublyLL.traverse()
doublyLL.reverse_traverse()
print(doublyLL.search(-10))
print(doublyLL.search(-20))
doublyLL.delete(-1)
print([node.value for node in doublyLL])
doublyLL.append(40)
print([node.value for node in doublyLL])
doublyLL.prepend(-20)
print(doublyLL.get(-1))
print(doublyLL.get(2).value)
print(doublyLL.get(20))
print(doublyLL.set(4, 50))
print(doublyLL)
print(doublyLL.pop_first().value)
print(doublyLL.pop().value)
print(doublyLL)
print(doublyLL.remove(2))
print(doublyLL)