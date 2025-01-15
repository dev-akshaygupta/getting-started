### Majority Element ###
# Find the Majority element in an array 

# Brute force solution - O(N^2)
def get_majority(arr):
	arr_ln = len(arr)
	for i in range(arr_ln-1):
		count = 1
		for j in range(i, arr_ln-1):
			if arr[i] == arr[j]:
				count += 1
		if count > arr_ln//2:
			return arr[i]
	return None

arr = [3, 3, 4, 2, 4, 4, 2, 4]
print(get_majority(arr))

# Sorted array solution - O(N logN)
def get_majority_sorted(arr):
	pass

arr = [3, 3, 4, 2, 4, 4, 2, 4]
print(get_majority(arr))