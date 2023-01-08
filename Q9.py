import mysql.connector as m
mycon=m.connect(host='localhost', user='root', password='yourpasswd', database='school')
mycur=mycon.cursor()
mycur.execute("select subject,code from exam order by subject")
for row in mycur:
    s,c=row
    print(s,'(',c,')', sep='')
mycur.close()
