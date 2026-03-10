N = int(input())

dp = [[0] * 10 for i in range(N + 1)]

for j in range(1, 10):
    dp[1][j] = 1

for x in range(2, N + 1):
    for y in range(10):
        if y == 0:
            dp[x][y] = dp[x - 1][1]
        elif y == 9:
            dp[x][y] = dp[x - 1][8]
        else:
            dp[x][y] = dp[x - 1][y - 1] + dp[x - 1][y + 1]

print(sum(dp[N]) % 1000000000)
