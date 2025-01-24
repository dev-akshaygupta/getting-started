### Remove duplicates from a sorted linked list ###

"""
Given a linked list sorted in non-decreasing order. 
Return the list by deleting the duplicate nodes from the list. 
The returned list should also be in non-decreasing order.

Input : Linked List = 11->11->11->21->43->43->60
Output : 11->21->43->60	(After removing duplicate elements)

Input : Linked List = 5->10->10->20
Output : 5->10->20 (After removing duplicate elements)
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

def remove_duplicates_inplace(head):
	 # Handle the empty list case
	if head is None:
		return None

	# Initialize pointers
	curr = head
	prev = head

	# Traverse the list to remove duplicates
	while curr:
		# If the current node is unique
		if curr.data != prev.data:
			prev.next = curr
			prev = prev.next
		curr = curr.next

	prev.next = None  # Terminate the modified list
	return head

first = Node(11)
second = Node(11)
third = Node(21)
fourth = Node(43)
fifth = Node(43)
sixth = Node(50)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

print("LinkedList: ", end="")
print_nodes(first)
new_list = remove_duplicates_inplace(first)
print_nodes(new_list)