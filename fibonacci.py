T = int(input("Enter the number of terms"))
n1,n2 = 0,1
while T>0 :
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    T-=1
    
