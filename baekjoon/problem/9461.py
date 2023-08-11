T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dp = [0] * 101
    dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2
    if N >= 5:
        for i in range(5, N+1):
            dp[i] = dp[i-1] + dp [i-5]
    
    print(dp[N])