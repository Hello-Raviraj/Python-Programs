sea=[]
x=int(input("enter the length"))
for i in range(x):
    y=int(input("enter thr number in d list"))
    sea.append(y)

print(sea)
b=list(set(sea))                   #using list is another way as list dont contain duplicates
print(b)


sea=list(dict.fromkeys(sea))      #dictonary dont keep duplicate keys
print(sea)
