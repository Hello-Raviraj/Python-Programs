sea=[]
x=int(input("enter the length"))
for i in range(x):
    y=int(input("enter thr number in d list"))
    sea.append(y)

print(sea)
sea=list(dict.fromkeys(sea))      #dictonary dont keep duplicate keys
print(sea)
