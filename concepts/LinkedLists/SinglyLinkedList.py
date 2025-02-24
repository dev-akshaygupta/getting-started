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
	return new_node


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


"""
Given a Linked List, the task is to delete a node 
in this given Linked List at the following positions: 

- At the front of the linked list
- At a specific position.
- At the end of the linked list.
"""

# At the front of the linked list
def delete_from_begining(head):

	# If the linked list is initially empty
	if head is None:
		return None

	# Change the head pointer to the next node
    # and free the original head
	temp = head
	head = head.next

	# Free the original head
	del temp

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

print("Before deletion: ", end="")
print_nodes(first)
head = delete_from_begining(first)
print("After deletion: ", end="")
print_nodes(head)
print()


# At a specific position.
def delete_at_position(head, pos):
	temp = head
	prev = None

	# If the linked list is initially empty
	if head is None:
		return None

	if pos == 1:
		head = temp.next
		return head

	# Traverse till given position
	for idx in range(1, pos):
		prev = temp
		temp = temp.next
		if temp is None:
			print("Data not present")
			return head

	# If given position is found, delete node
	if temp is not None:
		prev.next = temp.next
	return head


	# Change the head pointer to the next node
	# and free the original head
	temp = head
	head = head.next

	# Free the original head
	del temp

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

print("Before deletion: ", end="")
print_nodes(first)
head = delete_at_position(first, 5)
print("After deletion: ", end="")
print_nodes(head)
print()


# from end of the linked list
def delete_at_end(head):
	# If the list is empty, return None
	if head is None:
		return head

	# If the list has only one node, delete it and return None
	if head.next is None:
		return None

	# Find the second last node
	second_last = head
	while second_last.next.next:
		second_last = second_last.next

	# Delete the last node
	second_last.next = None
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

print("Before deletion: ", end="")
print_nodes(first)
head = delete_at_end(first)
print("After deletion: ", end="")
print_nodes(head)
print()


"""
Given a linked list and a key, 
the task is to check if key is present in the linked list or not. 

- Iteratively
- Recursively
"""

# Iteratively
def search_node_iteratively(head, key):
	curr = head
	
	# Iterate over all the nodes
	while curr.next is not None:
		
		# If the current node's value is equal to key,
        # return true
		if curr.data == key:
			return True
		curr = curr.next

	# If there is no node with value as key, return false
	return False

first = Node(10)
second = Node(62)
third = Node(43)
fourth = Node(74)
fifth = Node(95)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print(search_node_iteratively(first, 74))


# Recursively
def search_node_recursively(head, key):
	# Base case
	if head is None:
		return False

	# If key is present in current node, return true
	if head.data == key:
		return True

	return search_node_recursively(head.next, key)

first = Node(10)
second = Node(62)
third = Node(43)
fourth = Node(74)
fifth = Node(95)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print(search_node_recursively(first, 95))


"""
Given a Singly Linked List, 
the task is to find the Length of the Linked List.

- Iteratively
- Recursively
"""

def count_node_iteratively(head):
	curr = head
	count = 0
	
	# Iterate over all the nodes
	while curr is not None:
		count += 1
		curr = curr.next

	return count

first = Node(10)
second = Node(62)
third = Node(43)
fourth = Node(74)
fifth = Node(95)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print(count_node_iteratively(first))


def count_node_recursively(head):
	# Base case
	if head is None:
		return 0

	# Count this node plus the rest of the list
	return 1 + count_node_recursively(head.next)


first = Node(10)
second = Node(62)
third = Node(43)
fourth = Node(74)
fifth = Node(95)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print(count_node_recursively(first))


"""
Given a linked list, 
the task is to reverse the linked list by changing the links between nodes.

- Iteratively
- Recursively
- Using Stacks
"""

def reverse_iteratively(head):
	curr = head
	prev = None

	# Traverse all the nodes of Linked List
	while curr is not None:

		# Store next
		next_node = curr.next
		
		# Reverse current node's next pointer
		curr.next = prev
		
		# Move pointers one position ahead
		prev = curr
		curr = next_node

	return prev

first = Node(10)
second = Node(62)
third = Node(43)
fourth = Node(74)
fifth = Node(95)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Before reversal: ", end="")
print_nodes(first)
head = reverse_iteratively(first)
print("After reversal: ", end="")
print_nodes(head)
print()

def reverse_recursively(head):
	if head is None or head.next is None:
		return head

	# reverse the rest of linked list and put the 
    # first element at the end
	rest = reverse_recursively(head.next)

	# Make the current head as last node of 
    # remaining linked list
	head.next.next = head

	# Update next of current head to NULL
	head.next = None

	return rest

first = Node(10)
second = Node(62)
third = Node(43)
fourth = Node(74)
fifth = Node(95)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Before reversal: ", end="")
print_nodes(first)
head = reverse_recursively(first)
print("After reversal: ", end="")
print_nodes(head)
print()

def reverse_using_stacks(head):
	stack = []	# Create stack
	temp = head

	 # Push all nodes except the last node into stack
	while temp.next is not None:
		
		# append the top value of stack in list
		stack.append(temp)
		temp = temp.next

	# Make the last node as new head of the linked list
	head = temp

	# Pop all the nodes and append to the linked list
	while stack:
		temp.next = stack.pop()
		temp = temp.next
	
	# Update the next pointer of last node 
    # of stack to None
	temp.next = None

	return head


first = Node(10)
second = Node(62)
third = Node(43)
fourth = Node(74)
fifth = Node(95)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Before reversal: ", end="")
print_nodes(first)
head = reverse_using_stacks(first)
print("After reversal: ", end="")
print_nodes(head)
print()


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, value):
		self.head = Node(value)
		self.tail = self.head
		self.length = 1

	def __str__(self):
		curr = self.head
		result = ''
		while curr:
			result += str(curr.data)
			if curr.next:
				result += ' -> '
			curr = curr.next
		return result

	def prepend(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = self.head
		else:
			new_node.next = self.head
			self.head = new_node
		self.length += 1

	def append(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = self.head
		else:
			self.tail.next = new_node
			self.tail = new_node
		self.length += 1

	def insert(self, value, idx):
		new_node = Node(25)
		if idx < 0 or idx > self.length:
			return None
		if self.length == 0:
			self.head = new_node
			self.tail = self.head
		elif idx == 0:
			new_node.next = self.head
			self.head = new_node
		else:	
			curr = self.head
			for _ in range(idx-1):
				curr = curr.next
			new_node.next = curr.next
			curr.next = new_node
		self.length += 1

	def traverse(self):
		curr = self.head
		while curr:
			print(curr.data)
			curr = curr.next

	def search(self, target):
		curr = self.head
		while curr:
			if curr.data == target:
				return True
			curr = curr.next
		return False
	
	def get(self, idx):
		if idx == -1:
			return self.tail
		if idx < -1 or idx >= self.length:
			return None
		curr = self.head
		for _ in range(idx):
			curr = curr.next
		return curr
	
	def set_value(self, idx, value):
		node = self.get(idx)
		if node:
			node.data = value
			return True
		return False
	
	def pop_first(self):
		if self.length == 0:
			return None
		
		popped_node = self.head
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.head = self.head.next
			popped_node.next = None
		self.length -= 1
		return popped_node
	
	def pop(self):
		if self.length == 0:
			return None
		popped_node = self.tail
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			curr = self.head
			while curr.next is not popped_node:
				curr = curr.next
			self.tail = curr
			curr.next = None
			self.length -= 1

		return popped_node

	def remove(self, index):
		if index >= self.length or index < -1:
			return None
		if index == 0:
			return self.pop_first()
		if index == self.length-1 or index == -1:
			return self.pop()
		prev = self.get(index-1)
		popped_node = prev.next
		prev.next = popped_node.next
		popped_node.next = None
		self.length -= 1
		return popped_node

	def delete_all(self):
		self.head = None
		self.tail = None
		self.length = 0


new_linked_list = LinkedList(10)
new_linked_list.prepend(5)
new_linked_list.append(35)
new_linked_list.append(55)
new_linked_list.append(45)
new_linked_list.append(85)
new_linked_list.append(75)
new_linked_list.insert(25, 3)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.search(15))
print(new_linked_list.get(10))
new_linked_list.set_value(3, 43)
print(new_linked_list)
print(new_linked_list.pop_first().data)
print(new_linked_list.pop().data)
print(new_linked_list.remove(-1).data)
print(new_linked_list.delete_all())
print(new_linked_list)