#프로그래머스
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    memo = {}
    
    for i in participant:
        if i in memo :
            memo[i] += 1
        else : 
            memo[i] =1
    for i in completion:
        if i in memo:
             memo[i] -= 1
    for key, value in memo.items():
        if value == 1:
            return key
        
            
result = solution(participant, completion)
print(result)