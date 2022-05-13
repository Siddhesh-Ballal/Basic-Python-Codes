def Prime_till(n):
    l=[]
    for i in range(2,n+1):
        primeflag = 1;
        for j in range(2,i):
            if i%j==0:
                primeflag = 0
                break
        if(primeflag):
            l.append(i)
    return l


n = int(input("Enter number: "))
print("Prime numbers till ",n," is: ",Prime_till(n))
