import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sArr = sorted(set(arr))

dic= {value: idx for idx, value in enumerate(sArr)}

for j in arr:
    print(dic[j], end=' ')
