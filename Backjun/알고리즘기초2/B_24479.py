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

