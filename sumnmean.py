a = [12,3,5,-1,4]
i = 0
x = len(a)
sumi = 0
while(i <= x):
    
    if(a[i] == -1):
            break
    sumi = sumi + a[i]
    i += 1
    
print("Sum of the given 3 numbers is :",sumi)

print("Mean of the given 3 numbers is :",round((sumi/(i)),2))
      
    