### Longest sub string of 0’s in a binary string which is repeated K times ###

# Brute force - O(N)
def LongestZeroSubstring(string, str_ln, k):
	if k > 1:
		string += string
		str_ln *= 2

	count = 0
	max = 0

	for s in string:
		if s == "0":
			count += 1
		elif count > 0 and s == "1":
			if count > max:
				max = count
			count = 0
	return max


string = "0010001000"
str_ln = len(string)
k = 3

print(LongestZeroSubstring(string, str_ln, k))