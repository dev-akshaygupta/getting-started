### Check if a string contains a palindromic sub-string of even length ###
# Brute force solution - O(N^3)
def check_palindromic_substring(string, str_ln):
	slow = 0
	fast = 1

	while slow < str_ln:
		if fast < str_ln:
			substring = string[slow:fast]
			if substring == substring[::-1] and len(substring) > 0 and (len(substring) % 2 == 0):
				return True
				fast += 1
			else:
				fast += 1
		else:
			slow += 1
			fast = slow

	return False

string = 'aassss'
str_ln = len(string)
print(check_palindromic_substring(string, str_ln))