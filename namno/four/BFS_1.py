# 미션1: 방문시에 cur_v 출력하기
# 미션2: 5번 노드 방문할 때, '찾았다!'
from collections import deque

graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}
def bfs(graph, start_v):
    #초기 세팅
    q = deque()

    #시작점 예약
    q.append(start_v)
    visited = {start_v: True} #배열로 만들기 : visitied=[False] * len(graph)
    
    while q:
        #방문
        cur_v = q.popleft()
        print(cur_v) #미션 1

        #예약
        if cur_v == 5 : print("찾았다!")  #미션2
        for next_v in graph[cur_v]:
            if next_v not in visited :
                q.append(next_v)
                visited[next_v] = True

        

bfs(graph, 0)
