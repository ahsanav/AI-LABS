cgpa={}
cgpa["rafay"]=3.5
cgpa["arsalan"]=2.9
cgpa["asghar"]=1.5

for k in cgpa.keys():
    if(cgpa[k]<2.5):
        print("No Degree for",k)
    else:
        print("Degree will be awarded to",k)
