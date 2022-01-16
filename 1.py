f = open("source/01.txt", "r")
for x in f:
    print(x.count('(') - x.count(')'))
f.close()