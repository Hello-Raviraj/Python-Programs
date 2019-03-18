n=[5,2,1,7,3]                     #list to be sorted
for j in range(len(n),0,-1):      #iterartion for placing an values
    for i in range(j-1):          # iteration for comparision
        if n[i]>n[i+1]:
            temp=n[i]               #temp varible for swapping
            n[i]=n[i+1]
            n[i+1]=temp
print(n)
