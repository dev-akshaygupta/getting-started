str1 = "aab"
str2 = "aaaab"

count = 0
for idx_str1 in range(len(str1)):
	str3 = ""

	for idx_str2 in range(idx_str1, len(str1)):
		str3 = str1[idx_str2]
		print(idx_str2, str3)

		if str2.find(str3) != -1:
			count += 1
print(count)