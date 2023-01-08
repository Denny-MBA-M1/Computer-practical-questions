import mysql.connector as m
mycon=m.connect(host="localhost", user="root", password="yourpasswd", charset='UTF8')
mycur=mycon.cursor()
mycur.execute('drop database school')
mycur.execute('create database school')
mycur.execute('use school')
mycur.execute('create table student(rollno int, name varchar(10), gender char, srank int)')
for i in range(3):
    id=int(input("Enter the roll number"))
    name=input("Enter the name")
    gender=input("gender")
    srank=int(input("Enter the rank"))
    mycur.execute(f"insert into student values({id}, '{name}', '{gender}', {srank})")
mycon.commit()
mycur.execute("select * from student")
for x in mycur:
    print(x)
mycur.close()
