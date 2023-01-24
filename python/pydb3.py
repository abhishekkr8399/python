import pymysql
db=pymysql.connect("172.16.2.3","student","student","student")
cursor=db.cursor()
sql="SELECT * FROM Employee164;"
#sql="SELECT * FROM Employee WHERE income > '%d'" %(1000)
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
        print("First name = %s  Last name = %s  Age = %d  Sex = %s  Income = %f" %(fname,lname,age,sex,income))
except:
    print("Error occured while fetching the data.")
db.close()
