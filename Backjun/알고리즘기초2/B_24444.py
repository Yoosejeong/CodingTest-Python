from collections import deque
import sys
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N+1)
for i in range(1, N + 1):
    graph[i].sort()
def bfs(graph, start, visited):
    que = deque([start])
    index = 1
    visited[start] = index
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                index+=1
                visited[i] = index
                que.append(i)
bfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])