import sys
N, M = map(int, sys.stdin.readline().split())
nSet = set()
for i in range(N):
    nSet.add(sys.stdin.readline())
result = 0
for j in range(M):
    s = sys.stdin.readline()
    if s in nSet:
        result+=1

print(result)