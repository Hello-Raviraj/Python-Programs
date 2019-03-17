for i in range(5):        #for row iteration
  for n in range(i+1):    #for creating pattern of spaces like pattern2.instead of *,jst put an space.
    print(" ",end="")  
  for x in range(5-i):    #for creating actual pattern
    print("*",end="")
  print()
  
  
  #The idea behind this pattern is first create a pattern2(check in my repository) with spaces
  #and after that take another loop for printing actual pattern.
