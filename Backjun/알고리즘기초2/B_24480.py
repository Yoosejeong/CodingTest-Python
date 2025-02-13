import sys
N, M, R = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(150000)
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, N+1):
    graph[j].sort(reverse = True)

visited = [0] * (N+1)

index = 0
def dfs(graph, start, visited):
    global index
    index += 1
    visited[start] = index
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited)
            
dfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])
