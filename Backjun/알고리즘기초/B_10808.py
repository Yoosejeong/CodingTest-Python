import sys
s = sys.stdin.readline().strip()
result = [0] * 26
for i in s:
    a = ord(i)
    result[a%97] += 1

print(' '.join(map(str, result)))
    