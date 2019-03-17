list=[]                                       #empty list to store user input
n=int(input("Enter the length of an list"))
for i in range(n):
    x=int(input("Enter the values"))
    list.append(x)                            #to put an values in empty list

s=int(input("Enter the value to be search"))
def search(list):                             #function for linear search
    for value in list:
        if value==s:
            return True
if search(list):
    print("found")
else:
    print("not found")
