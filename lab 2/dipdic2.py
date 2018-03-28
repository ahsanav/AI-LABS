x={}
x["rafay"]=3.5
x["arsalan"]=2.9
x["asghar"]=1.5
n=input("Enter Name:")
for n in x.keys():
    if n in x.keys():
        x[n]+=1
    else:
        x[n]=1
print(n)