import sys
import re
s = sys.stdin.readline().strip()
arr=[]
result = []
arr = re.findall(r"<[^>]+>|[^<]+", s)
for i in arr:
    if i[0] == "<":
        result.append(i)
    else:
        li=[]
        li = i.split()
        count=0
        for k in li:
            count+=1
            result.append(k[::-1])
            if len(li) >= 2 and count!=len(li):
                result.append(" ")
print(''.join(result))