file1=open("text1.txt","w")
file2=open("text2.txt","w")
file3=open("text3.txt","w")
print("Press enter to stop exedcution")
while True:
    ch=input("Enter character")
    if ch=='':
        print("The contents in the file are:")
        break
    elif ch.islower():
        file1.write(ch)
    elif ch.isupper():
        file2.write(ch)
    else:
        file3.write(ch)
file1.close()
file2.close()
file3.close()
file=open("text1.txt")
print("the contents in file 1 are")
print(file.read())
file.close()
file=open("text2.txt")
print("the contents in file 2 are")
print(file.read())
file.close()
file=open("text3.txt")
print("the contents in file 3 are")
print(file.read())
file.close()
