N,M = map(int, input().split())
chess = [input() for _ in range(N)]

w = 'W', 'B'
b = 'B', 'W'

def check(i,j):
    result_w = 0
    result_b = 0
    for di in range(8):
        for dy in range(8):
            ni = di+i
            ny = dy+j
            if chess[ni][ny] != w[(di+dy)%2]:
                result_w+=1
            if chess[ni][ny] != b[(di+dy)%2]:
                result_b+=1
    return min(result_w, result_b)

result = 1000000
for i in range(N-7):
    for j in range(M-7):
        result = min(result, check(i,j))

print(result)