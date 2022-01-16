from itertools import groupby
s = "1113222113"
for i in range(40):
    l = list(s)
    grouped = [str(sum(1 for i in g)) + k for k,g in groupby(l)]
    s = "".join(grouped)
print(len(s))
