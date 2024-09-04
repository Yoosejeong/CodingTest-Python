participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    memo = {}
    for i in completion:
        memo[i] = True
    
    for i in participant:
        if i in memo:
             del memo[i]
             print(memo)
        elif i not in memo:
            return i
            
result = solution(participant, completion)
print(result)