import sys
n = int(sys.stdin.readline())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else : 
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 3
    for i in range(3, n+1):
        arr[i] = arr[i-1] + 2*(arr[i-2])
    print(arr[-1]%10007)
