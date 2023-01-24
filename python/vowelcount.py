vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
count=0
str=input("Enter a string : ")
for i in str.lower():
 if i in 'aeiou':
  vowels[i]=vowels[i]+1
  count=count+1
print("Total number of vowels : ",count)
print("Vowel occurences : ")
for vow in vowels:
 if(vowels[vow]>0):
  print(" ",vow," --> ",vowels[vow]," times")
