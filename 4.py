f = open("source/4 (1).txt", "r")
result = 0
for x in f:
    nums = sorted([int(i) for i in x.strip().split('x')])
    result += 2*(nums[0]*nums[1]+nums[1]*nums[2]+nums[0]*nums[2]) + nums[0]*nums[1]
f.close()
print("Total square:", result)