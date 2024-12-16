import sys
n, k = map(int, sys.stdin.readline().split())
arr = []
for i in range(1, n+1):
    arr.append(i)
result = []
index = 0
while arr:
    index += k-1
    if index>=len(arr):
        index = index%len(arr)
        result.append(arr.pop(index))
    else :
        result.append(arr.pop(index))
print("<", end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print(">")