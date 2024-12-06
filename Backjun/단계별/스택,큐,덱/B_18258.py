from collections import deque
import sys
que = deque()
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().strip()
    if s == "front":
        if que :
            print(que[0])
        else : 
            print(-1)
    elif s == "back":
        if que:
            print(que[-1])
        else :
            print(-1)
    elif s == "size":
        print(len(que))
    elif s == "empty":
        if que :
            print(0)
        else :
            print(1)
    elif s == "pop":
        if not que:
            print(-1)
        else :
            print(que[0])
            que.popleft()
    else : 
        a = s.split()
        que.append(a[1])
