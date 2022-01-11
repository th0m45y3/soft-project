f = open("source/1 (1).txt", "r")
for x in f:
    print(x.count('(') - x.count(')'))
f.close()