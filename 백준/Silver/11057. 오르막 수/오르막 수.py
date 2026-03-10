N = int(input())

dp = [[0] * 10 for i in range(N + 1)]

for j in range(0, 10):
    dp[1][j] = 1

for x in range(2, N + 1):
    for y in range(10):
        for z in range(0, 10 - y):
            dp[x][y] += dp[x - 1][y + z]

print(sum(dp[N]) % 10007)
