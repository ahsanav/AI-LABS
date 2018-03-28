g={}
g[1] = [2,3,5]
g[2] = [4,5]
g[3] = [2,4]
g[4] = [1,5]
g[5] = []

l=[1]
visited = []
while len(l) !=0:
    f = l[0]
    l.pop(0)
    if(f not in visited):
        visited.append(f)
    for i in g[f]:
        if(i not in visited):
           l.insert(0,i)
print(visited)
