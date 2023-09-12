N = int(input())
M = int(input())
arr = [i for i in range(1, N+1)]
vip_idx = [-1]
normal_cnt_list = []
for _ in range(M):
    vip_idx.append(int(input())-1)
vip_idx.append(N)
# print(arr)
# print(vip_idx)
ans = 1
dp = [0]*41
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(1, M+2):
    # print(vip_idx[i] - vip_idx[i-1] - 1)
    temp = vip_idx[i] - vip_idx[i-1] - 1
    ans *= dp[temp]

print(ans)

