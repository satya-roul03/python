import pymysql
try:
    con=pymysql.connect(host="localhost",database="student",user="root",password="Satya111@")
    cur=con.cursor()
    query="create table s(roll int(5) primary key,name varchar(16),mark double(5,2))"
    cur.execute(query)
    print("The table is created")
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("The problem is : ",e)
finally:
    if cur:
        cur.close()
    if con:
        con.close()  
