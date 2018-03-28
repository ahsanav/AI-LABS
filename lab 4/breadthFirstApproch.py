list = {}
list["1"] = ["2","5"]
list["2"] = ["12","52"]
list["3"] = ["4","2"]
list["4"] = ["2","6"]
list["5"] = ["8","9"]
list["6"] = ["10","12"]
list["7"] = ["6","5"]

l = ["1"]
processed=[]
while len(l) != 0:
    n = list(1)
    list.pop(1)
    processed.append(n)
    adjacent = list[n]
    l.append(adjacent)
print(processed)


