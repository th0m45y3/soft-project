f = open("source/passwords.txt", "r")
array = []
for x in f:
    line = x.strip().split(' ')
    for i in range(len(line)):
        for k in range(i + 1, len(line)):
            if (line[k] == line[i]):
                if not(line in array):
                    array.append(line)
print(len(array))
f.close()