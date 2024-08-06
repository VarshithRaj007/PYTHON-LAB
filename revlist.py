l=[]
n = int(input("Enter the number of values"))
for i in range(n):
	ele = int(input("Enter the elements"))
	l.append(ele)
l.reverse()
print("Reversed list:",l)
