### Equilibrium Index ###

# Brute force solution - Time: O(N^2), Space: O(1)
def get_equilibrium_index(arr):
	arr_ln = len(arr)

	for idx in range(arr_ln):
		leftsum = sum(arr[:idx])
		rightsum = sum(arr[idx+1:])

		if leftsum == rightsum:
			return arr[idx]
	
	return None

arr = [-7, 1, 5, 2, -4, 3, 0]
print(get_equilibrium_index(arr))

# Prefix Sum and Suffix Sum Array - Time: O(N), Space: O(N)
def get_equilibrium_PS(arr):
	arr_ln = len(arr)

	pref = [0] * arr_ln
	suff = [0] * arr_ln

	# Initial the start and end of prefix and suffix array
	pref[0] = arr[0]
	suff[arr_ln - 1] = arr[arr_ln - 1]

	# Calculate prefix sum for all indices
	for idx in range(1, arr_ln):
		pref[idx] = pref[idx - 1] + arr[idx]

	# Calculate suffix sum for all indices
	for idx in range(arr_ln - 2, -1, -1):
		suff[idx] = suff[idx + 1] + arr[idx]

	# Check if prefix sum equals to suffix sum
	for idx in range(arr_ln):
		if pref[idx] == suff[idx]:
			return arr[idx]

	return None

arr = [-7, 1, 5, 2, -4, 3, 0]
print(get_equilibrium_PS(arr))

# Prefix Sum and Suffix Sum Array (Efficient) - Time: O(N), Space: O(1)

def get_equilibrium_PS_Eff(arr):
	arr_ln = len(arr)
	arr_total = sum(arr)
	pref = 0

	for idx in range(arr_ln):
		suff = arr_total - pref - arr[idx]
		print(pref, suff)
		if pref == suff:
			return arr[idx]
		pref += arr[idx]

	return None

arr = [-7, 1, 5, 2, -4, 3, 0]
print(get_equilibrium_PS_Eff(arr))
