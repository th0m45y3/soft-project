f = open("source/3 (1).txt", "r")
result = 0
for x in f:
    line = sorted(x.strip().split('\t'), key=int)
    result += int(line[-1]) - int(line[0])
f.close()
print(result)