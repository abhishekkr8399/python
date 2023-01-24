filename=input("Enter the file name : ")
try:
 file=open(filename,"r")
 count=0
 print("Student | Total | Average")
 for line in file.readlines():
  count+=1 #count students
 score=0
 line=line.split(' ')
 for mark in line:
  score+=int(mark)
 print("\t%d \t %d \t %.2f" %(count,score, score/len(line)))
 file.close()
except FileNotFoundError:
 print("Invalid filename!")