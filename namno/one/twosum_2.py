#딕셔너리
nums = [4, 1, -4, -2, 9, 7, 5, 3, 16]
target = 14
def solution(nums, target):
    answer = 0
    memo = {} #빈 해시맵 만들기

    #O(n)
    #memo에 nums값과 True 넣기
    for num in nums:
        memo[num] = True

    print(memo)
    #O(n)
    for num in nums:
        need = target - num

        if need in memo and need != num :
            answer +=1
            del memo[need] 
            del memo[num]

    return answer

result = solution(nums, target)
print(result)