import random
y=random.randint(1,9)
count=0
x=0
while x != y:
    x = int(input("enter the number"))
    count=count+1
    if x > y:
        print("too high")
    elif x < y:
        print("too low")
    elif x==y:
        print ("exact")

print (y)
print(count)
