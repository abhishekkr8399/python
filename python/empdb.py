import pymysql #download pymysql if not exists
def Insert():
 db = pymysql.connect ("172.16.2.3","student","student"," EmployeeDB ") #Here EmployeeDB is DB name
 cursor = db.cursor()
 ssn=int(input("Enter employee ssn : "));
 fname=input("Enter first name : ");
 lname=input("Enter last name : ");
 age=int(input("Enter the age : "));
 place=input("Enter the place : ");
 salary=int(input("Enter the salary : "));
 sql = "INSERT INTO Employee VALUES(%d,'%s','%s',%d,'%s',%d)" %(ssn,fname,lname,age,place,salary)
 try:
  cursor.execute(sql)
  db.commit()
  print("Successfully inserted.")
 except:
  print("Unsuccessful!")
  db.close()
def Delete():
 db = pymysql.connect ("172.16.2.3","student","student"," EmployeeDB ") #Here EmployeeDB is DB name
 cursor = db.cursor()
 ssn=int(input("Enter the SSN : "))
 sql ="DELETE FROM Employee WHERE ssn=%d" %(ssn)
 try:
  cursor.execute(sql)
  db.commit()
  print("Deleted Successfully.")
 except:
  print("Unsuccessful!")
  db.close()
def Update():
 db = pymysql.connect ("172.16.2.3","student","student"," EmployeeDB ") #Here EmployeeDB is DB name
 cursor = db.cursor()
 ssn=int(input("Enter the ssn : "));
 fname=input("Enter first name : ");
 lname=input("Enter last name : ");
 age=int(input("Enter the age : "));
 place=input("Enter the place : ");
 salary=int(input("Enter the salary : "));
 try:
  cursor.execute("update EMPLOYEE set fname='%s',lname='%s',age=%d,place='%s',salary=%d where 
  ssn=%d"%(fname,lname,age,place,salary,ssn))
  db.commit()
  print("Successfully updated")
except:
 print("Unsuccessful!")
 db.close()
while True:
 print("\n1.Insert\t2.Delete \t3.Update\t4.Exit")
 n=int(input("Enter the choice : "))
 if n==1:
 Insert()
 elif n==2:
 Delete()
 elif n==3:
 Update()
 elif n==4:
 break
 else:
 print("Invalid choice")