import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for j in range(1, N+1):
    graph[j].sort()
visited = [False] * (N+1)
visited2 = [False] * (N+1)
result = [] * N
result2 = [] * N
def bfs(graph, start, visited):
    visited[start] = True
    que = deque([start])
    while que:
        a = que.popleft()
        result.append(a)
        for i in graph[a]:
            if not visited[i] :
                visited[i] = True
                que.append(i)

def dfs(graph, start, visited2):
    visited2[start] = True
    result2.append(start)
    for i in graph[start]:
        if not visited2[i]:
            dfs(graph, i, visited2) 
bfs(graph, V, visited)
dfs(graph, V, visited2)

for i in result2:
    print(i, end=' ')
print()
for j in result:
    print(j, end=' ')    