import math

dp = [0] * 1023
for i in range(10):
    dp[i] = i
print(dp)
idx = 0
for i in range(10):
    for j in range(10):

        dp[idx] = value