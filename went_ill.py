import numpy as np
dic = {}
delay = []

def funcy (x):
    res = x.strip()
    x = res.split(" ")
    if (x[0].isdigit()) & (len(x) == 3):
        dic[x[2]] = np.uint16(x[0])
    elif (len(x) == 3) & (x[0] in dic):
        dic[x[2]] = dic[x[0]]
        if (res) in delay:
            delay.remove(res)
    else:
        if(x[0] == "NOT"):
            if (x[1] in dic):
                dic[x[-1]] = ~np.uint16(dic[x[1]])
                if (res) in delay:
                    delay.remove(res)
            else:
                if (res) not in delay:
                    delay.append(res)
        else:
            if (((x[0] in dic) | (x[0].isdigit())) & ((x[2] in dic) | x[2].isdigit())):
                a = np.uint16(dic[x[0]]) if x[0] in dic else np.uint16(x[0])
                b = np.uint16(dic[x[2]]) if x[2] in dic else np.uint16(x[2])
                match x[1]:
                    case "AND":
                        el = a & b
                    case "OR":
                        el = a | b
                    case "LSHIFT":
                        el = a << b
                    case "RSHIFT":
                        el = a >> b
                if (res) in delay:
                    delay.remove(res)
                dic[x[-1]] = el
            else:
                if (res) not in delay:
                    delay.append(res)

f = open("source/wires.txt", "r")
for x in f:
    funcy(x)
f.close()

for c in range(150):
    for x in delay:
        funcy(x)

print(dic)
print(delay)

