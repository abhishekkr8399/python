class Account():
 def __init__(self,accno):
  self.__accno=accno
  self.__bal=100
 def withdraw(self,amt):
  if(amt > (self.__bal-100)):
   print("Insufficient Balance.")
  else:
   self.__bal -= amt
 print(amt,"debited successfully.")
 def deposit(self,amt):
  self.__bal += amt
 print(amt,"credited successfully.")
 def getBalance(self):
  return self.__bal
 def getAccount(self):
  return self.__accno
def exists(account,accno): #this method is not a part of class
 flag=0
 for acc in account:
  if accno == acc.getAccount():
   return acc
 return None
account=[]
while True:
 print("\n1.Create account 2.Withdraw 3.Deposit 4.Display Max Balance 5.Exit")
 choice=int(input("Enter your choice:"))
 if choice==1:
  accno=int(input("Enter the Acc No : "))
  if exists(account,accno) != None:
   print("Account already exists.")
  else:
   obj=Account(accno)
   account.append(obj)
   print("Account created successfully.")
 elif choice==2:
  accno=int(input("Enter the Acc No : "))
  acc=exists(account,accno)
  if acc==None:
   print("Account not found.");
  else:
   amt=int(input("Enter the amount : "))
   acc.withdraw(amt)
 elif choice==3:
  accno=int(input("Enter the Acc No : "))
  acc = exists(account, accno)
  if acc == None:
   print("Account not found.");
  else:
   amt=int(input("Enter the amount : "))
   acc.deposit(amt)
 elif choice==4:
  accnt=account.sort(key=lambda x:x.getBalance(),reverse=True)
  print("Account with maximum balance:",account[0].getAccount(),"and balance is:",account[0].getBalance())
 elif choice==5:
  break
 else:
  print("Invalid choice!")