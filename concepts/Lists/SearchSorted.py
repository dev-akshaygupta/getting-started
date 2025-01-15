### Searching in a Sorted List using Binary Search 	###
def binary_search(ls, start, end, key):
	if start < end:
		
		# Floor division to find mid index
		mid = (start + end) //2

		# Checks for key
		# if key is mid, we'll return mid index
		# if key is on the left, we'll discard right side of the list and look further on left side
		# if key is on the right, we'll discard left side of the list and look further on right side
		if key == ls[mid]:
			return mid
		elif key < ls[mid]:
			return binary_search(ls, start, mid-1, key)
		elif key > ls[mid]:
			return binary_search(ls, mid+1, end, key)

	return -1

# Let us take a sorted array to find a key
arr = [4, 11, 20, 39, 44, 57, 63, 72, 88, 94]
key = 72

idx = binary_search(arr, 0, len(arr)-1, key)
if idx != -1:
	print("Key is found at index: " + str(idx))
else:
	print(f"Given key {key} not found")