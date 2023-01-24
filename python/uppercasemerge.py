str1=input("Enter string-1 : ")
str2=input("Enter string-2 :" )
res=""
for char in str1:
 if char.isupper():
  res+=char
for char in str2:
 if char.isupper():
  res+=char
print("Resultant String is ",res)
