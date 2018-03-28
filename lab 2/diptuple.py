'''x = (1,9,8)
#x[0] = 50
x = (1,5,8)
print(x)
for i in x:
    print(i)'''


z = ['win','loss','loss','loss','win']
l = len(z)
win = 0
for i in z:
    if i =='win':
        win = win+1
print(win)
ratio = win/l
print(ratio)


