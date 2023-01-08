file=open("text1.txt","w")
ch="y"
while ch=="y":
    gettext=input("Enter text")
    file.write(gettext+"\n")
    ch=input("do u want to continue")
file.close()
file=open("text1.txt","r")
lines=file.readlines()
file.close()
file1=open("text2.txt","w")
file2=open("text3.txt","w")
for line in lines:
    if 'a' in line or 'A' in line:
        file1.write(line)
    else:
        file2.write(line)
file1.close()
file2.close()
file=open("text2.txt")
for line in file:
    print("Lines with a or A")
    print(line, end="")
file.close()
file=open("text3.txt")
print("Lines w/o A")
for line in file:
    print(line, end="")
file.close()

        
