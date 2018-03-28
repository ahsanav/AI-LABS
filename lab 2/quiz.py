l = [False]*1001
i = 2
prime=[]
while(i<1000):
    if(l[i]==False):
        prime.append(i)
        for j in range(i,1001,i): l[j] = True
    i=i+1
print(prime)