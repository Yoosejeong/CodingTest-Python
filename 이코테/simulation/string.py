S = list(input())
S.sort()

arr = []
sum=0
for i in S:
    if i.isalpha():
        arr.append(i)
    else : sum += int(i)
arr.append(str(sum))
print(''.join(arr))