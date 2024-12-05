import sys

while True:
    que = []
    result = "yes"
    s = sys.stdin.readline().rstrip()
    if s =="." :
        break
    for i in s:
        if i == "(" or i== "[":
            que.append(i)
        elif i=="]" :
            if que and que[-1] == "[":
                que.pop()
                break
            else :
                result = "no"
                break
        elif i == ")":
            if que and que[-1] == "(":
                que.pop()
                break
            else :
                result = "no"
                break
    print(result)
    
    