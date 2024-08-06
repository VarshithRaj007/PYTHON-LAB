l=[]
n = int(input("Enter the number of values"))
for i in range(n):
	ele = int(input("Enter the elements"))
	l.append(ele)
even=[]
odd=[]
for ele in l:
	if ele % 2 == 0:
		even.append(ele)
	else:
		odd.append(ele)
print("Even numbers :",even)
print("Odd numbers:",odd)
