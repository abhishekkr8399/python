filename=input("Enter the file name : ")
try:
  file=open(filename,"r")
  lines=words=chars=0
  for i in file.readlines():
   lines+=1 #Increment line count
   for w in i.split(" "):
    if len(w)>0 and w!='\n': #To ignore empty words and \n
      words+=1
      for c in w:
        if c!='\n': # TO ignore \n at the end of each lines while counting
           chars+=1
    print("Number of lines : ",lines)
    print("Number of words : ",words)
    print("Number of characters (Excluding spaces and \\n) : ",chars)
    file.close()
except FileNotFoundError:
    print("Invalid filename!")
