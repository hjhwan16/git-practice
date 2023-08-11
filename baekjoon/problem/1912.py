# 연속합 / DP / 20230811

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(N-1):
    dp[i] = arr[i] + arr[i+1]

print(max(dp))