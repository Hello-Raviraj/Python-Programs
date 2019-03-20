x="hello"
x.casefold()
y=reversed(x)          #reversed function return reverse object

if list(x)==list(y):        #so for comparision we convert them into list and then compare
  print("its palindrome")
else:
  print("no palindrome")
