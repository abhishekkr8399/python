str=input("Enter a string : ")
pmarks="\'!()-[]{};:\".,\\<>/?@#$%^&*_~" #some characters(“ ‘ /) preceded with slash to escape their meaning
res=""
for i in str:
 if i not in pmarks:
  res+=i
print("Original string : ",str)
print("String after modification : ",res)
