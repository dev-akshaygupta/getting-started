###	Leaders in an array	###

# Brute force solution - O(N^2)
def leader(arr):
	arr_ln = len(arr)
	result = []

	for i in range(arr_ln):
		flag = 0
		for j in range(i+1, arr_ln):
			if arr[i] < arr[j]:
				break
		else:
			result.append(arr[i])
	return result

arr = [16, 17, 4, 3, 5, 2]
print(leader(arr))


# Efficient solution - O(N)
def leader_eff(arr):
	arr_ln = len(arr)
	result = []

	# Start with the rightmost element
	maxRight = arr[-1]

	# Rightmost element is always a leader
	result.append(maxRight)

	# Traverse the array from right to left
	for i in range(arr_ln-2, -1, -1):
		if arr[i] >= maxRight:
			maxRight = arr[i]
			result.append(maxRight)

	result.reverse()
	return result

arr = [16, 17, 4, 3, 5, 2]
print(leader_eff(arr))
