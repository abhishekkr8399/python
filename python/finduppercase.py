str=input("Enter a string : ");
letters=[]
position=[]
for i in range(len(str)):
 if(str[i].isupper()):
  letters.append(str[i])
  position.append(i)
print("Number of capitals letters : ",len(letters))
print("Letter --- Position")
for i in range(len(letters)):
 print(" ",letters[i],"\t\t\t",position[i])
