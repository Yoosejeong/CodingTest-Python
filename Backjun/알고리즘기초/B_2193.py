import sys
n = int(sys.stdin.readline())

if n == 1:
    print(1)
elif n== 2:
    print(1)
else :
    d = [0]*(n+1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n+1):
        d[i] = d[i-2]+d[i-1]
    print(d[n])