import mysql.connector as m
mycon=m.connect(host="localhost", user="root", password="yourpasswd", database="school")
mycur=mycon.cursor()
rollno=int(input("Enter the roll no of the student to search for"))
mycur.execute(f"select * from student where rollno={rollno}")
x=mycur.fetchone()
if x==None:
    print("Not a valid roll number")
else:
    print("Deleting")
    print("Id-",x[0], "name",x[1], "gender",x[2], "rank", x[3])
    mycur.execute(f"delete from student where rollno={rollno}")
    mycon.commit()
    print("successfully deleted")
    print("New Student Table")
    mycur.execute("select * from student")
    for i in mycur:
        print(i)
mycur.close()
