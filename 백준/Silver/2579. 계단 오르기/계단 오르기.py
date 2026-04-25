N = int(input())
stairs = [int(input()) for _ in range(N)]

dp = [[0] * 3 for _ in range(N + 1)]
dp[1][1] = stairs[0]
for i in range(2, N + 1):
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + stairs[i - 1]
    dp[i][2] = dp[i - 1][1] + stairs[i - 1]

print(max(dp[N][0], dp[N][1], dp[N][2]))