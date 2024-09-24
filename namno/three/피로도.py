from itertools import permutations
dungeons = [[80,20],[50,40],[30,10]]
k=80

def solution(k, dungeons):
    max = 0    
    temp_k = k
    for i in permutations(dungeons, len(dungeons)):
        k = temp_k
        answer=0
        for j in range(0,len(dungeons)):
            if i[j][0] <=k:
                k = k-i[j][1]
                answer+=1
        if max <= answer : max = answer
    return max
result = solution(k, dungeons)
print(result)