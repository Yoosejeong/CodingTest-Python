from collections import deque

def solution(begin, target, words):
    answer = 0
    if not target in words:
        return 0
    return bfs(begin, target, words)
        
        

def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = [False]*len(words)
    while queue:
        word, step = queue.popleft()
        if target == word:
            return step
        for i in range(len(words)):
            if not visited[i]:
                count = 0
                for j in range(len(word)):
                    if word[j] == words[i][j]:
                        count+=1
                if count == len(begin)-1:
                    step +=1
                    queue.append([words[i],step])
                    visited[i] = True
    return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]	
    
step = solution(begin, target, words)
print(step)    
