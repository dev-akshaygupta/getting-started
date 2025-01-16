### Majority Element ###
# Find the Majority element in an array 

# Brute force solution - Time: O(N^2), Space: O(1)
def get_majority(arr):
	arr_ln = len(arr)
	
	for i in range(arr_ln-1):
		count = 1
		
		for j in range(i, arr_ln-1):
			if arr[i] == arr[j]:
				count += 1
		
		if count > arr_ln//2:
			return arr[i]
	
	# No majority found
	return None

arr = [1, 1, 2, 1, 3, 5, 1]
print(get_majority(arr))

# Sorted array solution - Time: O(N logN), Space: O(1)
def get_majority_sorted(arr):
	arr_ln = len(arr)

	if arr_ln == 1:
		return arr[0]

	count = 1
	arr.sort()

	for idx in range(1, arr_ln):
		if arr[idx - 1] == arr[idx]:
			count += 1 
		else:
			if count > arr_ln//2:
				return arr[idx - 1]
			count = 1
	
	# Check the last element 
	if count > arr_ln//2:
			return arr[- 1]

	# No majority found
	return None

arr = [1, 1, 2, 1, 3, 5, 1, 3, 3, 3, 3, 3, 3]
print(get_majority_sorted(arr))

# Using Hashing – Time: O(n), Space: O(N)
def get_majority_hashmap(arr):
	arr_ln = len(arr)

	hashmap = {}

	for num in arr:
		if num not in hashmap:
			hashmap[num] = 1
		else:
			hashmap[num] += 1

		if hashmap[num] > arr_ln//2:
			return num
	return None

arr = [1, 1, 2, 1, 3, 5, 1]
print(get_majority_hashmap(arr))

# Moore’s Voting Algorithm- Time: O(n), Space: O(1)
def get_majority_mooresvoting(arr):
	arr_ln = len(arr)
	candidate = arr[0]
	count = 1

	# Get majority candidate 
	for idx in range(1, arr_ln):
		if count == 0:
			candidate = arr[idx]
			count += 1

		if arr[idx] == candidate:
			count += 1
		else:
			count -= 1

	# Check majority candidate
	count = 0 
	for num in arr:
		if num == candidate:
			count += 1

	# If count is greater than n / 2
	# return the candidate; otherwise, return None
	if count > arr_ln//2:
		return candidate
	return None

arr = [1, 1, 2, 1, 3, 5, 1, 3, 3, 3, 3, 3, 3]
print(get_majority_mooresvoting(arr))