N = int(input())

dp = [0] * (N + 1)
route = [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    route[i] = i - 1
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        route[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        route[i] = i // 2
        
print(dp[N])
start = N
print(start, end = " ")
while route[start]:
    print(route[start], end = " ")
    start = route[start]