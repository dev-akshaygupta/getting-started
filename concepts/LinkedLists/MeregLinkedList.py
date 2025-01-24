### Merge two sorted linked lists ###

"""
Given two sorted linked lists consisting of n and m nodes respectively. 
The task is to merge both of the lists and return the head of the merged list.

Input: 
head1: 1 -> 5 -> 6 -> 8
head2: 2 -> 4 -> 7 -> 9

Output: 1 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
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

# Inplace O(n+m), O(1)
def merge_lists_inplace(head1, head2):
	if head1 is None:
		return head2
	if head2 is None:
		return head1

	# Determine the starting point of the merged list
	if head1.data < head2.data:
		merged_head = head1
		head1 = head1.next
	else:
		merged_head = head2
		head2 = head2.next

	tail = merged_head

	# Traverse both lists and merge them
	while head1 and head2:
		if head1.data < head2.data:
			tail.next = head1
			head1 = head1.next
		else:
			tail.next = head2
			head2 = head2.next
		tail = tail.next

	# Append the remaining nodes from the non-empty list
	if head1:
	    tail.next = head1
	if head2:
	    tail.next = head2
	
	return merged_head


def merge_lists_recursion(head1, head2):
	# Base case
	if head1 is None:
		return head2
	if head2 is None:
		return head1

	if head1.data <= head2.data:
		head1.next = merge_lists_recursion(head1.next, head2)
		return head1
	else:
		head2.next = merge_lists_recursion(head1, head2.next)
		return head2

first = Node(5)
second = Node(6)
third = Node(8)
fourth = Node(9)

fifth = Node(2)
sixth = Node(3)
seventh = Node(7)
eigth = Node(10)

first.next = second
second.next = third
third.next = fourth

fifth.next = sixth
sixth.next = seventh
seventh.next = eigth

print("LinkedList: ")
print_nodes(first)
print_nodes(fifth)
print_nodes(merge_lists_inplace(first, fifth))
print_nodes(merge_lists_recursion(first, fifth))