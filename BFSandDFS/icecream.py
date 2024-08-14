#NXM형태의 얼음틀에서 구멍 뚫린 부분은0, 칸막이 존재하는 부분은 1.
#구멍이 뚫린 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결된 것.
#얼음 틀의 모양 주어졌을때 생성되는 총 아이스크림의 개수를 구하기


N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list((map(int,input()))))
print(arr)