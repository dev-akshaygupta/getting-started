### Detect and Remove Loop in Linked List ###

"""

Given the head of a linked list that may contain a loop.  
A loop means that the last node of the linked list is connected back to a node in the same list. 
The task is to remove the loop from the linked list (if it exists).

"""

class Node:
	def __init__(self, data):
		self.data =  data
		self.next = None

def print_nodes(node):
	if node is None:
		return None

	while node is not None:
		print(node.data, end=" ")
		node = node.next
	print()

# - Using hashset - O(N), O(N)
def remove_loops_hashset(head):
	if head is None or head.next is None:
		return

	hashset = set()
	prev = None

	# Function to detect and remove loop from linked list
	while head:
		# If node is already in the set, remove the loop
		if head in hashset:
			prev.next = None
			return
		
		# Add node to the set and move forward
		hashset.add(head)
		prev = head
		head = head.next

# - Using slow and fast pointer - O(N), O(1)
def remove_loops_SF(head):
	if head is None or head.next is None:
		return

	slow = head
	fast = head

	# Move slow pointer by 1
	# Move fast pointer by 2
	while slow and fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		# If slow meets fast, loop is detected
		if slow == fast:

			# Find the node where loop started
			while slow != fast:
				slow = slow.next
				fast = fast.next

			# Find node where loop ended
			# remove it
			while fast.next != slow:
				fast = fast.next
			fast.next = None

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

first.next = second
second.next = third
third.next = fourth
fourth.next = third

print("LinkedList: ", end="")
remove_loops_hashset(first)
print_nodes(first)