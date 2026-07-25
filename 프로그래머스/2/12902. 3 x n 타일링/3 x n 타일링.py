def solution(n):
    dp = [0] * 5001
    dp[0] = 1
    dp[2] = 3
    dp[4] = 11
    for i in range(6, n + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(0, i - 3, 2):
            dp[i] += dp[j] * 2
        
    answer = dp[n] % 1000000007
    
    return answer