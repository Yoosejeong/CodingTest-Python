#각 자리가 0~9로 이루어진 문자열 S가 주어질 때, 왼쪽에서 오른쪽으로 하나씩 모든 숫자 확인
#숫자 사이에 x나 + 넣어서 만들어질 수 있는 가장 큰 수 구함. 

S = input()

result = int(S[0])

for i in range(1, len(S)):
    num = int(S[i])
    if result <=1 or num<=1 :
        result += num
    else : result *= num

print(result)