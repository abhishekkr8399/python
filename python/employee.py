def monthlyPay(week_hours,hourly_pay,weeks):
 monthly_pay=week_hours*hourly_pay*weeks
 return monthly_pay
name=input("Enter employee name : ")
id=input("Enter employeee ID : ")
week_hours=int(input("Enter weekly working hours : "))
hourly_pay=int(input("Enter pay rate per hour : "))
weeks=int(input("Enter total number of weeks : "))
print("\nEmployee Details")
print("Employee Name : ",name)
print("Employee ID : ",id);
print("Monthly Pay : ",monthlyPay(week_hours,hourly_pay,weeks))