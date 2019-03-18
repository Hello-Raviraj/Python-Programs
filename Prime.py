def search(n):
    for i in range(2,n):
        if n%i==0:
            return True
n=13
if search(n):
    print("its not prime")
else:
    print("irs prime")
