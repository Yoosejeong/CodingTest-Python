N = int(input())

arr = input().split(' ')

X=1
Y=1

#L R U D 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in arr:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx = X+dx[i]
            ny = Y+dy[i]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    X, Y = nx, ny
print(X, Y)