import sys
a, b = map(int, sys.stdin.readline().split())
dic = {}
aArr = set(map(int,sys.stdin.readline().split()))
bArr = set(map(int,sys.stdin.readline().split()))
result = 0
for i in aArr:
    if i not in bArr:
        result +=1
for j in bArr:
    if j not in aArr:
        result+=1
#for 문 없이 len(aArr-bArr)+len(bArr-aArr)로 가능
print(result)