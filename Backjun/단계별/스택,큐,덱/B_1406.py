from collections import deque
import sys

left_stack = deque()
right_stack = deque()
n = sys.stdin.readline().strip()
for i in n:
    left_stack.append(i)
m = int(sys.stdin.readline().strip())
for _ in range(m):
    x = sys.stdin.readline().strip()
    if x == "L" and left_stack:
        right_stack.appendleft(left_stack[-1])
        left_stack.pop()
    elif x == "D"and right_stack:
        left_stack.append(right_stack[0])
        right_stack.popleft()
    elif x == "B" and left_stack:
        left_stack.pop()
    elif x[0] == "P" :
        a, b = x.split()
        left_stack.append(b)
    else:
        continue
for j in left_stack:
    print(j, end='')
for k in right_stack:
    print(k, end='')
