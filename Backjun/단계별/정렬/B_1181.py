import sys
n = int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(sys.stdin.readline().strip())

strings = sorted(set(arr), key = lambda x: (len(x), x))
for a in strings:
    print(a)