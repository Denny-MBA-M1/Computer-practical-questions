import mysql.connector as m
mycon=m.connect(host="localhost", user="root", password="yourpasswd", database="school")
mycur=mycon.cursor()
rollno=int(input("Enter roll no to search for"))
mycur.execute(f"select * from student where rollno={rollno}")
x=mycur.fetchone()
if x==None:
    print("Wrong roll no")
else:
    print("Updating")
    print("id-",x[0], "name-",x[1], "gender-", x[2], "rank", x[3])
    rank=int(input("Enter the new rank"))
    mycur.execute(f"update student set srank={rank} where rollno={rollno}")
    mycon.commit()
    mycur.execute("select * from student")
    for x in mycur:
        print(x)
mycur.close()
