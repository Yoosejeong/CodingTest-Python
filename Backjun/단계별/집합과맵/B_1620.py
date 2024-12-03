import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for i in range(1, n+1):
    x = sys.stdin.readline().strip()
    dic[i] = x
    dic[x] = i
arr=[]
for k in range(m):
    j = sys.stdin.readline().strip()
    if j.isdigit():
        arr.append(dic[int(j)])
    else :
        arr.append(dic[int(j)])   
for l in arr:
    print(l)