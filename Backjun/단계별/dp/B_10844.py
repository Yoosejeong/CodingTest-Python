import sys

MOD = 1000000000  # 10^9로 나눈 나머지

N = int(sys.stdin.readline().strip())

dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1  


for i in range(2, N+1):  
    dp[i][0] = dp[i-1][1]  
    dp[i][9] = dp[i-1][8]  
    for j in range(1, 9): 
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD


result = sum(dp[N]) % MOD
print(result)