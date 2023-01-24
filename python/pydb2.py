import pymysql
db=pymysql.connect("172.16.2.3","student","student","student")
cursor=db.cursor()
sql="INSERT INTO Employee164 VALUES('Sumit','',20,'M',5000000)"
try:
    cursor.execute(sql)
    db.commit()
    print("Insertion successful.")
except:
    db.rollback()
    print("Error occured while inserting the values to the database.")
db.close()
