### Find the longest substring with k unique characters in a given string ###

# Brute Force - O()
def unique_longest_substring(string, str_ln, k):


string = "aabbcc"
k = 2
str_ln = len(string)

print(unique_longest_substring(string, str_ln, k))