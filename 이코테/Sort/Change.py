#두 배열 A,B가 있다. N개의 원소로 구성돼있으며, 모두 자연수이다. 
#최대 K번의 바꿔치기 연산 수행할 수 있는데, A와 B의 원소 하나 골라 바꾸는 것이다.
#최종 목표는 배열 A의 모든 원소 합이 최대가 되는 것이다. 
#최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값 출력.

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i]<B[i] :
        A[i], B[i] = B[i], A[i]
    else : break

print(sum(A))