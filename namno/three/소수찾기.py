from itertools import permutations


numbers = "011"

def solution(numbers):
    answer = 0 

    setc = set()  # 중복된 순열을 방지하기 위한 set

    # 1부터 numbers의 개수까지 반복하기.
    # numbers에서 i개만큼 반복해서 순열을 생성하기
    # set에 넣기
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            setc.add(int(''.join(p)))
 
    # setc에서 하나씩 꺼내서 모두 반복하기
    for i in setc :
         # 만약 2보다 작으면 continue(소수는 1 포함 안됨)
         if i<2:
             continue
         # 소수 여부를 True로 초기화
         is_prime = True
         # 2부터 int(i의 제곱근)까지 반복하기(소수판정)
         # 만약 i를 j로 나누었을 때 나머지가 0이면 소수가아님.
         for j in range(2, int(i**0.5)+1):
             if i % j ==0:
                is_prime = False
                break # 이미 소수가 아니므로 더 소수판별 하지말고 break (다른 setc 내의 숫자 검사하기)
         # is_prime이 True면 answer+1을 해준다. 
         if is_prime : answer+=1
             
    
    return answer

result = solution(numbers)
print(result)