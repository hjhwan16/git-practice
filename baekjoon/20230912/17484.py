
def dfs(i, j, d, ans, tot):
    if i == N-1:
        return min(ans, tot)
    dj = [-1, 0, 1]
    for k in range(3):
        ni = i + 1
        nj = j + dj[k]
        if k != d and 0 <= ni < N and 0 <= nj < M:
            ans = dfs(ni, nj, k, ans, tot + arr[ni][nj])
    return ans


N, M = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
start_list = []
for i in range(M):
    start_list.append([0, i])
ans = 1e10



for start in start_list:
    ans = min(dfs(start[0], start[1], -1, ans, arr[start[0]][start[1]]), ans)

print(ans)
