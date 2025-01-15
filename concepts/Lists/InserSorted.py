###	Insert in a Sorted List	###
def insert_sorted(arr, n, key, capacity):
	if n >= capacity:
		return n

	i = n-1
	while i >= 0 and arr[i] > key:
		arr[i+1] = arr[i]
		i -= 1
	arr[i+1] = key

	return n+1

# Let us take a sorted array to find a key
arr = [4, 11, 20, 39, 44, 57]
key = 42
n = 6

for i in range(10):
    arr.append(0)

capacity = len(arr)

print("Before insertion: ", end='')
for i in range(n):
	print(arr[i], end=' ')

n = insert_sorted(arr, n, key, capacity)

print("After insertion: ", end='')
for i in range(n):
	print(arr[i], end=' ')