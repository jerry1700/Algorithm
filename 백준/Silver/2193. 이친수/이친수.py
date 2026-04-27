N = int(input())

dp = [0] * (N + 1)
dp[1] = 1
if N >= 2:
    dp[2] = 1
if N >= 3:
    dp[3] = 2
for i in range(4, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    
print(dp[N])