arr = [[0 for x in range(1000)] for y in range(1000)]
f = open("source/lampsbrightness.txt", "r")
for x in f:
    lines = x.strip().split(' ')
    fromC = [int(lines[-2].split(',')[0]),int(lines[-2].split(',')[1])]
    toC = [int(lines[-1].split(',')[0]),int(lines[-1].split(',')[1])]
    if(lines[0] == "toggle"):
        for i in range(fromC[0], toC[0] + 1):
            for k in range(fromC[1], toC[1] + 1):
                arr[i][k] += 2
    elif (lines[1] == "on"):
        for i in range(fromC[0], toC[0] + 1):
            for k in range(fromC[1], toC[1] + 1):
                arr[i][k] += 1
    elif (lines[1] == "off"):
        for i in range(fromC[0], toC[0] + 1):
            for k in range(fromC[1], toC[1] + 1):
                if(arr[i][k] - 1 < 0):
                    arr[i][k] = 0
                else:
                    arr[i][k] -= 1 

        #for i in range(int():
f.close()
res = 0
for i in range(1000):
    for k in range(1000):
        res+=arr[i][k]
print(arr[498])
print(arr[499])
print(res)