f = open("source/02.txt", "r")
result = 0
for x in f:
    line = sorted(x.strip().split('\t'), key=int)
    for i in range(len(line)):
        for k in range(i + 1, len(line)):
            if (int(line[k]) % int(line[i]) == 0):
                result += int(line[k]) / int(line[i])
f.close()
print(result)