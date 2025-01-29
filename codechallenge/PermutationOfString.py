"""
Given a string s, which may contain duplicate characters, 
your task is to generate and return an array of all unique permutations of the string. 
You can return your answer in any order.

Examples:
Input: s = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
Explanation: Given string ABC has 6 unique permutations.

Input: s = "ABSG"
Output: ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", 
"BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", 
"GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", 
"SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
Explanation: Given string ABSG has 24 unique permutations.

Input: s = "AAA"
Output: ["AAA"]
Explanation: No other unique permutations can be formed as all the characters are same.

Constraints:
1 <= s.size() <= 9
s contains only Uppercase english alphabets
"""


def findPermutation(s):
	result = []
	s = sorted(s)							# Sort the string to handle duplicates

	def backtrack(path, used):
		# Base case: If the current permutation (path) is of the same length as the input string
		if len(path) == len(used):
			result.append(''.join(path)) 	# Join the path as a string and add it to result
			return

		# Loop through each character in the string to build permutations
		for i in range(len(s)):
			# If the character at index 'i' is already used, skip it
			if used[i]:
				continue

			# Skip duplicates: If the current character is the same as the previous one and the previous one wasn't used
			if i > 0 and s[i] == s[i-1] and not used[i-1]:
				continue

			# Mark the character at index 'i' as used
			used[i] = True

			# Recursively build the next part of the permutation by adding the character at index 'i' to the path
			backtrack(path + [s[i]], used)

			# After exploring this path, backtrack by marking the character as unused
			used[i] = False

	used = [False] * len(s)
	backtrack([], used)
	return result

print("Total permutations are: ", len(findPermutation("ABSG")))
print(findPermutation("ABSG"))