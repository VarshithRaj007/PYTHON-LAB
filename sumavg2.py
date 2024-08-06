l=[]
n = int(input("Enter the number of values"))
for i in range(n):
	ele = int(input("Enter the element"))
	l.append(ele)
avg =sum(l)/len(l)
print(sum(l))
print("Avg=",avg) 
