#factorial using recursion

def fact(n):
  if n==0:            #we have to put limit that is n==0 as fact(0) is always 1.if we dont put limit it will take negative numbers as well 
    return 1
  else:
    
    z=n * fact(n-1)
    return z
z=fact(5)
