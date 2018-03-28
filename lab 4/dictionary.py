g = {}
g["1"] = ["4","6"]
g["2"] = ["1","6"]
g["3"] = ["2","3"]
g["4"] = ["4","5"]
g["5"] = ["6","7"]
x = input("Enter Number:")
print(len(g[x]))
c = 0
for i in g.keys():
    if(x in g[i]):
       c += 1
print(str(c))




