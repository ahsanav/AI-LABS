g={}
g[1] = [2,5]
g[2] = [3,4,5,6]
g[3] = [6]
g[4] = [5]
g[5] = [3,7]
g[6] = [1]
g[7] = [3,6]

l = [1]
visited=[]
while len(l) != 0:
    f = l[0]
    l.pop(0)
    if(f not in visited):
        visited.append(f)
    for i in g[f]:
        if(i not in visited):
            l.append(i)
print(visited)

