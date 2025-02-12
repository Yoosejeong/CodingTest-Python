def dfs(graph, start, visited):
    global index
    index += 1
    visited[start] = index
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited)
            
import sys

N, M, R = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [0] * (N+1)

index = 0

dfs(graph, R, visited)
for j in range(1, N+1):
    print(visited[j])
