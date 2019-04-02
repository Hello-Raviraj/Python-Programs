import random

s="123456789abcdeABCDE!@#$%"            #the complexity of password
len=4                                       #length of password
p="".join(random.sample(s,len))                 #join function to join the result otherwise it will create list.
print(p)                                               #random.sample to create random output of given length
