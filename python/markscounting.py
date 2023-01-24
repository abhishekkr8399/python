try:
 answer=open("keys.txt","r").readline().split()
 file=open("marks.txt","r")
 max=0
 for marks in file.readlines():
  marks = marks.split()
  name = marks[0]
  count = 0
 for i in range(1, len(marks)):
  if marks[i] == answer[i]:
   count += 1
   print(name, " Marks : ", count)
 if count>max:
  max=count
  max_student=name
  print("\nStudent with maximum marks :")
  print(max_student," Marks : ",max)
except FileNotFoundError:
 print("File not found.");