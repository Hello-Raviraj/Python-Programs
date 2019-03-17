for i in range(5):            #for row iteration
  for n in range(5-i):        #for creating pattern of spaces like pattern1.instead of *,jst put an space.
    print(" ",end="")
  for x in range(i+1):        #for creating actual pattern.
    print("*",end="")
  print()                     #for new line 
