def indexOfSmallestElement(lst):
 index=lst.index(min(lst))
 return index+1
n=int(input("Enter the number of elemets : "))
lst=[]
for i in range(n):
 lst.append(int(input("Element-%d : " %(i+1))))
print("Index of smallest element is :", indexOfSmallestElement(lst))