import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
stack = []
arr = []
dic = {}
al=65
for j in range(n):
    k = int(sys.stdin.readline())
    dic[chr(al)] = k
    al+=1
for i in s:
    if i == "*" :
        b = stack.pop()
        a = stack.pop()
        x = a*b
        stack.append(x)
    elif i == "-":
        b = stack.pop()
        a = stack.pop()
        x = a-b
        stack.append(x)
    elif i == "+":
        b = stack.pop()
        a = stack.pop()
        x = a+b
        stack.append(x)
    elif i == "/":
        b = stack.pop()
        a = stack.pop()
        x = a/b
        stack.append(x)
    else :
        stack.append(dic[i])
result = float(stack[0])
result_num = f"{result:.2f}"
print(result_num)