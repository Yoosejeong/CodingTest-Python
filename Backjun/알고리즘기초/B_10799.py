import sys
s = sys.stdin.readline().strip()
stack = []
result=0
count=-1
for j in s:
    count+=1
    #"()"레이저인 경우
    if j == ")" and s[count-1]=="(":
        stack.pop()
        result+=len(stack)
        result=result-1
    elif j =="(":
        result+=1
        stack.append(j)
    else:
        stack.pop()

print(result)