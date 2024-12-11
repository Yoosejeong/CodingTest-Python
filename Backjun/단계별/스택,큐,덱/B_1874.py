import sys
n = int(sys.stdin.readline())
stack = []
arr = []
result = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

stack.append(1)
result.append("+")
index = 2
while arr:
    if not stack:
        stack.append(index)
        index+=1
    elif stack[-1] == arr[0]:
        stack.pop()
        arr.pop(0)
        result.append("-")
    elif stack[-1] > arr[0]:
            break

    else : 
        stack.append(index)
        result.append("+")
        index+=1


if arr :
    print("NO")

else : 
    for i in result:
        print(i)