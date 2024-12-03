import sys
n = int(sys.stdin.readline())
dic={}
for i in range(n):
    a, b =sys.stdin.readline().split()
    dic[a] = b

arr=[]
for key,value in dic.items():
    if value == "enter":
        arr.append(key)

arr.sort(reverse=True)  
for j in arr:
    print(j) 