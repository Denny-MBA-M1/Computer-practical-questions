file=open("rhyme.txt","w")
file.write('''Would i be ok if I took some of your time? Would it be ok if I wrote you a phyme''')
file.close()

file=open("rhyme.txt","r")
lines=file.readlines()
for line in lines:
    words=line.split()
    for word in words:
        print(word+'#', end='')
    print()
file.close()
