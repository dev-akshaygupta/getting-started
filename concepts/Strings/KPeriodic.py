### Check if the given string is K-periodic ###

# Brute force - O(N^2/k)
def is_K_periodic(k, string, str_ln):
	slow = 0
	fast = k

	while slow < str_ln:
		substring = string[slow:fast]
		if substring * (str_ln//k) == string:
			return True
		else:
			slow = fast + 1
			fast += k
	return False

string = "geeksforgeeksfor"
k = 8
str_ln = len(string)

print(is_K_periodic(k, string, str_ln))

# Efficient Approach - O(N)
def is_prefix(string, str_ln, idx, k):
	# k length sub-string cannot 
    # start at index idx
	if idx + k > str_ln:
		return False
	for idxj in range(0, k):
		if string[idx] == string[idxj]:
			return True
	return False

def is_K_periodic_eff(string, str_ln, k):
	# Check whether all the sub-strings
	# are equal to the k length prefix of the string 
	for idx in range(k, str_ln, k):
		if is_prefix(string, str_ln, idx, k):
			return True
	return False

string = "geeksforgeeksfor"
k = 8
str_ln = len(string)

print(is_K_periodic_eff(string, str_ln, k))