"""
Given a singly linked list, the task is to find the middle of the linked list. 
If the number of nodes are even, then there would be two middle nodes, 
so return the second middle node.

Input: linked list = 1 -> 2 -> 3 -> 4 -> 5
Output: 3 
Explanation: There are 5 nodes in the linked list and there is one middle node whose value is 3.

Input: linked list = 10 -> 20 -> 30 -> 40 -> 50 -> 60
Output: 40
Explanation: There are 6 nodes in the linked list, 
so we have two middle nodes: 30 and 40, but we will return the second middle node which is 40.
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

# Naive approach - O(N)
def find_middle_node_iter(head):
	curr = head
	count = 0

	while curr is not None:
		count += 1
		curr = curr.next

	pos = count//2

	for idx in range(pos + 1):
		if idx == pos:
			return head.data
		head = head.next


# Tortoise and Hare Algorithm - O(N)
def find_middle_node_SF(head):
	slow = head
	fast = head

	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next

	return slow.data


first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

print("LinkedList: ", end="")
print_nodes(first)
middle = find_middle_node_iter(first)
print(f"Middle node is: {middle}")
middle = find_middle_node_SF(first)
print(f"Middle node is: {middle}")