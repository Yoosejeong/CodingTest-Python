import sys
from collections import deque
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

for i in range(1, N+1):
    graph[i].sort(reverse = True)
def bfs(graph, start, visited):
    que = deque([start])
    index = 1
    visited[start] = index
    while que :  
        a = que.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                que.append(i)
                index +=1
                visited[i] = index

bfs(graph, R, visited)
for i in range(1, N+1):
    print(visited[i])