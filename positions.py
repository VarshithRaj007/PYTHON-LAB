l=[]
n = int(input("Enter the number of values"))
for i in range(n):
	ele = int(input("Enter the elements"))
	l.append(ele)
print("Max element in the list",max(l))
print("Min element in the list",min(l))
