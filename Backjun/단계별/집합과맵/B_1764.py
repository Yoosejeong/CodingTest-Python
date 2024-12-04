import sys
n, m = map(int, sys.stdin.readline().split())
nArr = []
mArr = []
for i in range(n):
    nArr.append(sys.stdin.readline().strip())
dic={key:0 for key in nArr}
for j in range(m):
    j = sys.stdin.readline().strip()
    if j in dic.keys():
        dic[j]+=1
result = []
for a,b in dic.items():
    if b>0:
        result.append(a)
result.sort()
print(len(result))
print(result)
for re in result:
    print(re)
