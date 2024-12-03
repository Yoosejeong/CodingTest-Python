#set을 활용하여 in 연산할 때 O(1)의 시간 복잡도 가지게 하기
import sys
n = int(sys.stdin.readline())
nArr = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mArr = list(map(int, sys.stdin.readline().split()))
for num in mArr:
    print(1 if num in nArr else 0, end=' ')