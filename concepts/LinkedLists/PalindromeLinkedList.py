"""
Given a singly linked list. The task is to check if the given linked list is palindrome or not.

Input: linked list = 1 -> 2 -> 1 -> 2 -> 1
Output: true
Explanation: The given linked list is 1 -> 2 -> 1 -> 2 -> 1, 
which is a palindrome and Hence, the output is true.

Input: linked list = 1 -> 2 -> 3 -> 4
Output: false
Explanation: The given linked list is 1 -> 2 -> 3 -> 4,
which is not a palindrome and Hence, the output is false.
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

# Using Stack - O(N), O(N)
def check_palindrome_stack(head):
	curr = head
	stack = []

	while curr is not None:
		stack.append(curr.data)
		curr = curr.next

	while stack:
		node_data = stack.pop()

		if head.data != node_data:
			return False

		head = head.next

	return True

# Using Recursion - O(N), O(N)
def check_palindrome_recursion(head):

	def is_palindrome(end, start):

		# Base case
		if end is None:
			return True

		# Recursively check right side
		right = is_palindrome(end.next, start)

		# Compare start and end nodes
		ans = right and start[0].data == end.data

		# Update start node
		start[0] = start[0].next

		return ans

	# Set starting head node
	start = [head]

	# Recursively check all and return
	return is_palindrome(head, start)

	

# Using Recursion - O(N), O(1)
def reverse(head):
	prev = None
	curr = head
	while curr:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	return prev

def is_identical(head1, head2):
	while head1 and head2:
		if head1.data != head2.data:
			return False
		head1 = head1.next
		head2 = head2.next
	return True

def check_palindrome_iteration(head):
	if head is None or head.next is None:
		return True

	slow, fast = head, head

	# Find the middle of the list
	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next

	# Split the list and reverse the second half
	head2 = reverse(slow.next)
	slow.next = None

	# Check if the two halves are identical
	check = is_identical(head, head2)

	## Restore the original list
	head2 = reverse(head2)
	slow.next = head2

	return check

first = Node(1)
second = Node(2)
third = Node(1)
fourth = Node(1)
fifth = Node(2)
sixth = Node(1)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

print("LinkedList: ", end="")
print_nodes(first)
print(check_palindrome_stack(first))
print(check_palindrome_recursion(first))
print(check_palindrome_iteration(first))