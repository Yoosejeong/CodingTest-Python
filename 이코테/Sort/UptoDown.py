N = int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
#arr = sorted(array, reverse=True)

for i in arr:
    print(i , end=' ')