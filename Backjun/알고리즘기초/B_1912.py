import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
d = [0]*n
d[0] = arr[0]
for i in range(1, n):
    d[i] = max(d[i-1]+arr[i], arr[i])
print(max(d))