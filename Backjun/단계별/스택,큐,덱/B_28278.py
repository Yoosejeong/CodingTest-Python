import sys
n = int(sys.stdin.readline())
que = []
for i in range(n):
    x = sys.stdin.readline().split()
    if x[0] == "2":
        if que :
            print(que[-1])
            que.pop()
        else : 
            print(-1)
    elif x[0] == "3":
        print(len(que))
    elif x[0] == "4":
        if que :
            print(0)
        else :print(1)
    elif x[0]== "5":
        if que :
            print(que[-1])
        else : 
            print(-1)
    else :
        que.append(x[1])