import pymysql
try:
    con=pymysql.connect(host="localhost",database="student",user="root",password="Satya111@")
    cur=con.cursor()
    query="update student set name='Satyajit' where roll=101"
    cur.execute(query)
    con.commit()
    query="select *from student"
    cur.execute(query)
    con.commit()
    data=cur.fetchone()
    while data is not None:
        print(data)
        data=cur.fetchone()
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("The problem is : ",e)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
