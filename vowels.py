#counting particular character from given string
#idea-first we have to create a empty dictonary by connecting it with what we need to count
#if its an vowels,we put that vowels in empty dictonary having an key as voewls and value initially 0
#by using an for loop,for every char er check if its an vowel or not
#if it is we increment the particular counter by 1

x="THis is my first program of python not really "
v="aeiou"
x=x.casefold()                 #for casesensitive
empty={}.fromkeys(v,0)
for char in x:
  if char in empty:
    empty[char]=empty[char]+1
prin(empty)
    
