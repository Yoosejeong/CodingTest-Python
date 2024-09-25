from collections import deque
class Solution:
    def numIslands(self, grid):
        #모든 좌표를 돌면서(노드1이면서, 방문한 적 없을때만) bfs() 실행 + count++
        #row_len은 grid의 요소의 개수.
        #col_len은 grid의 요소 하나 택하고 그거의 개수
        row_len, col_len = len(grid), len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]
        for r in range(row_len):
            for c in range(col_len):
                #if 1이면서, 방문한 적 없을 때만
                if gird[r][c] == 1 and not visited[r][c]
                #bfs() 실행 / count++
                bfs()
                answer +=1
        return answer
def bfs(self, start_r ,start_v, grid, visited):
    #초기세팅
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    queue = deque()
    #첫 노드 예약
    queue.append((start_r, start_v))
    visited[start_r][start_c]=True
    while q:
        #현재 노드 방문
        cur_r, cur_c = queue.popleft()
        #다음 노드 예약
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0<= next_r < len(grid) and 0<= next_c < len(grid[0]):
                if grid[nc]