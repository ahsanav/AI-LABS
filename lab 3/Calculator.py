def add(x,y):
    z = x+y
    print(z)
def sub(x,y):
    z = x-y
    print(z)
def mul(x,y):
    z = x*y
    print(z)
def div(x,y):
    z= x/y
    print(z)

x = int(input("Enter First number:"))
y = int(input("Enter Second number:"))
z = input("Enter Operator:")
if z == '+':
    add(x,y)
elif z == '-':
    sub(x,y)
elif z == '*':
    mul(x,y)
elif z == '/':
    div(x,y)
