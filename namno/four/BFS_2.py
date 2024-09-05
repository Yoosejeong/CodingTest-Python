# 미션3: 4번 노드 방문할 때, 몇번 만에 4번 노드에 도착할 수 있는지
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
    visited = {v: -1 for v in graph} #배열로 만들기 : visitied=[-1] * len(graph)
    visited[start_v] = 0
    
    while q:
        #방문
        cur_v= q.popleft()
        dist = visited[cur_v]
        print(cur_v, dist) #미션 1

        if cur_v == 4:
            print(f"4번 노드에 {dist}번 만에 도착!")

        #예약
        if cur_v == 5 : print("찾았다!")  #미션2
        for next_v in graph[cur_v]:
            if visited[next_v] == -1 :
                q.append(next_v)
                visited[next_v] = dist+1

        

bfs(graph, 0)
