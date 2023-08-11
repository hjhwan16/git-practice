# 부녀회장이 될테야

T = int(input())

for tc in range(1, T+1):
    k = int(input()) # 층
    n = int(input()) # 호
    dp = [[0] * (n + 1) for _ in range(k+1)]
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[k][n])
    

