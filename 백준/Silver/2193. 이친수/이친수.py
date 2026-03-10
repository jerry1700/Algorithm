N = int(input())

dp = [[0] * 10 for i in range(N + 1)]

dp[1][0] = 0
dp[1][1] = 1
for x in range(2, N + 1):
    dp[x][0] += dp[x - 1][0] + dp[x - 1][1]
    dp[x][1] += dp[x - 1][0]

print(sum(dp[N]))
