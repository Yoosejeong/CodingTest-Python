import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
stack.append(arr[0])
check = []
turn = 1
for i in arr:
    stack.append(i)

    while stack and stack[-1] == turn:
        stack.pop()
        turn+=1
if stack:
    print("Sad")
else :
    print("Nice")
