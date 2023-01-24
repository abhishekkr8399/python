import pymysql
db=pymysql.connect("172.16.2.3","student","student","student")
cursor=db.cursor()
sql="CREATE TABLE Employee164(f_name varchar(30) not null, l_name varchar(20), age int,sex char(1), income float)"
try:
    cursor.execute(sql)
    print("Table created successfully.")
except:
    print("Table already exists.")
db.close()
