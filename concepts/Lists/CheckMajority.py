### Check for Majority Element in a sorted list ###


# Using Linear Search
# Brute force solution - O(N)
def is_majority(arr, x):
	arr_ln = len(arr)
	counter = 0
	for num in arr:
		if num == x:
			counter += 1

	if counter > (arr_ln/2):
		return True
	return False

arr = [1, 2, 3, 3, 3, 3, 10]
x = 3
flag = is_majority(arr, x)
if flag:
	print("x is in majority")
else:
	print("x is not in majority")

# Efficient solution - O(N)
def is_majority_GFG(arr, x):
	arr_ln = len(arr)
	last_index = (arr_ln//2 + 1) if arr_ln%2 != 0 else (arr_ln//2)

	for i in range(last_index):
		if arr[i] == x and arr[i + arr_ln//2] == x:
			return True
	return False
arr = [1, 2, 3, 3, 3, 3, 10]
x = 3
flag = is_majority_GFG(arr, x)
if flag:
	print("x is in majority")
else:
	print("x is not in majority")


# Using Binary Search - O(log N)
def _binary_search(arr, start, end, key):
	if start <= end:
		mid = (start + end)//2

		if (mid == 0 or key > arr[mid-1]) and arr[mid] == key:
			return mid
		elif key > arr[mid]:
			return _binary_search(arr, mid+1, end, key)
		else:
			return _binary_search(arr, start, mid-1, key)
	return -1


def is_majority_BS_GFG(arr, x):
	arr_ln = len(arr)

	# index of first occurance of the key
	idx = _binary_search(arr, 0, arr_ln - 1, x)

	if idx == -1:
		return False

	# check if the key is present in more than n/2 of the array
	print(idx)
	print(idx + arr_ln//2)
	if ((idx + arr_ln//2) <= arr_ln-1) and arr[idx + arr_ln//2] == x:
		return True
	else:
		return False

arr = [1,1,1,1,1,1,1,2,3,4,5,6,6]
x = 1
flag = is_majority_BS_GFG(arr, x)
if flag:
	print("x is in majority")
else:
	print("x is not in majority")
