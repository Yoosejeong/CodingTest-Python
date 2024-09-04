#N이 1이 될때까지 두 과정 중 하나 반복 수행. 
#1. N에서 1을 뺌
#2. N을 K로 나눔. N이 K로 나누어떨어질때만 가능
#N, K 주어질 때 N이 1이될때까지 최소 횟수 구하기
N,K = map(int,input().split())
count = 0
while N!=1 :
    if N%K ==0 : 
        N = N//K
        count+=1
    else :
        N = N-1
        count+=1
print(count)
