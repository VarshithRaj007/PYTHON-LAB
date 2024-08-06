l=[]
n = int(input("Enter the number of values"))
for i in range(n):
	ele = int(input("Enter the elements"))
	l.append(ele)
rem=int(input("Enter the element to be removed"))

if rem in l:
	l.remove(rem)
else:
	print("Element is not on the list")

print("List after removing the element",l)

