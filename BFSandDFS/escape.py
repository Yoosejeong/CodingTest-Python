#NxM크기의 직사각형 형태의 미로가 갇혔다. 처음 위치는 (1,1) 미로 출구는 (N, M)
#한번에 한 칸 씩 이동할 수 있다. 괴물이 있는 부분은 0, 괴물 없는 부분은 1. 
#탈출하기 위해 움직여야하는 최소 칸의 개수를 구해라.
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft
        #상하좌우 탐색
        for i in range(4):
            nx = x+dx[x]
            ny = y+dy[y]
            #벗어나는 경우 무시
            if nx < 0 or nx>=N or ny<0 or ny>=M:
                continue
            #괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[N-1][M-1]


N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]
 
print(bfs(0,0))

