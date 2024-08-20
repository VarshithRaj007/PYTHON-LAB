input_string = input("Enter a string\n")
vow_count = 0
vow = "aeiouAEIOU"
for char in input_string:
	if char in vow:
		vow_count += 1
print("The number of vowels in the string are",vow_count)
