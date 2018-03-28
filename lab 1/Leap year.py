'''x = int(input("Enter Year:"))
if x%4==0:
    if(x%100==0):
        if(x%400==0):
            print("LEAP YEAR")
        else:
          print("NOT A LEAP YEAR")
    else:
           print("LEAP YEAR")
else:
     print("NOT A LEAP YEAR")'''


'''x = int(input("Enter Year:"))
if(x%4==0):
    if(x%100==0):
        if(x%400==0):
            print("Leap Year")
        else:
            print("Not A Leap Year")
    else:
        print("Leap Year")
else:
    print("Not A Leap Year")


x = int(input("Enter Year:"))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("Leap Year")
        else:
            print("Not a leap Year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")




x = input("Enter String:")
d=0
a=0
for i in x:
    if x.isdigit():
        d=d+1
    if x.isalpha():
        a=a+1
print("Digit:",d)
print("Letters:",a)'''


x = input("Enter Sentence:")
x = len(x.split())
print(x)






















