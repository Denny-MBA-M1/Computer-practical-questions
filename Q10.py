import mysql.connector as m
mycon=m.connect(host='localhost', user='root', password='yourpasswd', database='school')
mycur=mycon.cursor()
mycur.execute("select code,subject from exam where practical=30")
for x in mycur:
    print(x)
mycur.close()
