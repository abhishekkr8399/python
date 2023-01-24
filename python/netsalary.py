name=input("Enter employee name : ")
id=input("Enter employee ID : ")
basic=float(input("Enter basic salary : "))
allowances=float(input("Enter allowances : "))
gross_sal=basic+allowances
if gross_sal>20000:
 income_tax=gross_sal*0.3
elif gross_sal>10000:
 income_tax=gross_sal*0.2
elif gross_sal>5000:
 income_tax=gross_sal*0.1
else:
 income_tax=0
net_sal=gross_sal-income_tax
print("\nEmployee Details")
print("Employee Name : ",name)
print("Employee ID : ",id)
print("Basic Salary : ",basic)
print("Allowances : ",allowances)
print("Gross Salary : ",gross_sal)
print("Income Tax : ",income_tax)
print("Net Salary : ",net_sal)
