fib1=0
fib2=1
n=int(input("Enter the number of fibonacci numbers to be printed : "))
if n>0:
 print("First ",n," fibonacci numbers are : ")
 print(fib1, end=" ") #end line with space instead of \n
 if n>1: print(fib2, end=" ")
 for i in range(2,n):
    fib3=fib1+fib2
    print(fib3,end=" ")
    fib1=fib2
    fib2=fib3
else:
    print("Invalid choice!")