### Find common elements in three sorted arrays	###

a = [1, 5, 8, 10, 20, 30]
b = [5, 8, 13, 15, 20]
c = [5, 8, 20, 23]


# Brute force solution
# Time complexity: O(n1*log(n1) + n2*log(n1) + n3*log(n1)) = O((n1 + n2 + n3)*log n1)
def common_elements(a, b, c):
	hashmap = {}
	for ele in a:
		hashmap[ele] = 1

	for ele in b:
		if ele in hashmap and hashmap[ele] == 1:
			hashmap[ele] = 2

	for ele in c:
		if ele in hashmap and hashmap[ele] == 2:
			hashmap[ele] = 3

	common_ele = []
	for ele, count in sorted(hashmap.items()):
		if count == 3:
			common_ele.append(ele)

	return common_ele

print(common_elements(a, b, c))