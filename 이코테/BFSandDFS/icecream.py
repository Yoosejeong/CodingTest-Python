#NXM형태의 얼음틀에서 구멍 뚫린 부분은0, 칸막이 존재하는 부분은 1.
#구멍이 뚫린 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결된 것.
#얼음 틀의 모양 주어졌을때 생성되는 총 아이스크림의 개수를 구하기


N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list((map(int,input()))))

#DFS로 특정한 노드 방문한 뒤 연결된 모든 노드들도 방문
def dfs(x, y):
    #주어진 범위를 벗어나는 경우에 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않았으면
    if graph[x][y]==0:
        graph[x][y] == 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False



#모든 노드에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result +=1

print(result)