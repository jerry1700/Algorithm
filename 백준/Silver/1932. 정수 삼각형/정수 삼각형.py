n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * i for i in range(n + 1)]
dp[1][0] = nums[0][0]
if n >= 2:
    dp[2][0] = dp[1][0] + nums[1][0]
    dp[2][1] = dp[1][0] + nums[1][1]
for i in range(3, n + 1):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + nums[i - 1][j]
        elif j == i - 1:
            dp[i][j] = dp[i - 1][j - 1] + nums[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + nums[i - 1][j]

print(max(dp[n]))