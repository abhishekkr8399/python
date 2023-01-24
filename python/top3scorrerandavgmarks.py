marks={'John':86.5, 'Jack':91.2, 'Jill':84.5, 'Harry':72.1,'Joe':80.5}
sorted_keys=sorted(marks, key=marks.get, reverse=True)
print("Top 3 scorers : ")
for i in sorted_keys[:3]:
 print(i," : ",marks[i])
sum=0
for i in marks:
 sum+=marks[i]
avg=sum/5
print("\nTotal marks of all students : %.2f" %(sum))
print("Average of all marks = %.2f" %(avg))