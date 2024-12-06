from collections import deque
import sys
n = int(sys.stdin.readline())
deq = deque()
for i in range(n):
    s = sys.stdin.readline().strip()
    if s[0] == "1":   
        a = s.split()
        deq.appendleft(a[1])
    elif s[0] == "2":   
        a = s.split()
        deq.append(a[1])
    elif s == "3" :
        if deq :
            print(deq[0])
            deq.popleft()
        else :
            print(-1)
    elif s == "4" :
        if deq :
            print(deq[-1])
            deq.pop()
        else :
            print(-1)
    elif s == "5":
        print(len(deq))
    elif s == "6":
        if deq :
            print(0)
        else :
            print(1)
    elif s == "7":
        if deq:
            print(deq[0])
        else :
            print(-1)
    else :
        if deq:
            print(deq[-1])
        else :
            print(-1)
