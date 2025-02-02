import sys

n = int(sys.stdin.readline().strip())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 최대 사탕 개수를 찾는 함수
def get_max_candies(board):
    max_count = 1  # 최소한 1개의 사탕은 먹을 수 있음

    for i in range(n):
        row_count, col_count = 1, 1  # 같은 행과 열에서 연속된 사탕 개수

        for j in range(1, n):
            # 행 방향 체크
            if board[i][j] == board[i][j - 1]:
                row_count += 1
            else:
                max_count = max(max_count, row_count)
                row_count = 1

            # 열 방향 체크
            if board[j][i] == board[j - 1][i]:
                col_count += 1
            else:
                max_count = max(max_count, col_count)
                col_count = 1

        # 행, 열의 마지막까지 갔을 때 최댓값 갱신
        max_count = max(max_count, row_count, col_count)

    return max_count

# 사탕 교환 및 최대 사탕 개수 탐색
max_candy = get_max_candies(arr)  # 초기 상태에서 연속된 사탕 개수 체크

for i in range(n):
    for j in range(n - 1):
        # 가로로 인접한 두 사탕 교환
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        max_candy = max(max_candy, get_max_candies(arr))
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]  # 원래대로 복구

        # 세로로 인접한 두 사탕 교환
        arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
        max_candy = max(max_candy, get_max_candies(arr))
        arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]  # 원래대로 복구

print(max_candy)