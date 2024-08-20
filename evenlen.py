input_string = input("Enter a string\n")
words = input_string.split()
print("Even letter words are:")
for word in words:
	if (len(word)%2 == 0):
		print(word)
