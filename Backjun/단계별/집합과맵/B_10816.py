import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dic = {key:0 for key in arr}
for i in range(n):
    a = arr[i]
    dic[a] += 1 
m = int(sys.stdin.readline())
mArr = list(map(int, sys.stdin.readline().split()))
result = []
for i in mArr:
    if i in dic.keys():
        result.append(dic[i])
    else: 
        result.append(0)
for j in result:
    print(j, end=' ')