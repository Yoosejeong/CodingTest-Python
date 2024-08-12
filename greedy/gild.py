#모험가 길드에서 N명의 모험가 대상으로 '공포도'를 측정. 높은 모험가는 대처 능력 떨어짐.
#공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가가 그룹에 참여해야함.
#N명의 모험가에 대한 정보 주어질 때 여행 떠날 수 있는 그룹 수의 최댓값은?

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
count = 0

for i in arr:
    count += 1 #현재 그룹에 해당 모험가 포함
    if count >= i :
        result +=1
        count = 0
print(result)

