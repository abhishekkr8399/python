def binarySearch(elements,key):
 low=0
 high=len(elements)-1
 while low<=high:
  mid=int((low+high)/2)
 if elements[mid]==key:
  return mid
 elif key<elements[mid]:
  high=mid-1
 else:
  low=mid+1
 return -1
list=[]
n=int(input("Enter the number of element : "))
for i in range(n):
 list.append(int(input("Element-%d : " %(i+1))))
key=int(input("Enter the element to be searched : "))
list.sort()
print("Sorted List : ",list);
pos=binarySearch(list,key)
if pos != -1 :
 print("Key found at position ",pos+1)
else:
 print("Key not found!")
