import sys

n = int(sys.stdin.readline())
arr=[]
for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    arr.append((x,y))
arr.sort(key=lambda c: (c[0], c[1]))
for x,y in arr:
    print(x,y)