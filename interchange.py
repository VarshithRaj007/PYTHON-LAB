l=[]
n = int(input("Enter the number of values"))
for i in range(n):
	ele = int(input("Enter the elements"))
	l.append(ele)
if len(l)>0:
	l[0],l[-1] = l[-1],l[0]
print("The list after interchanging is",l)

