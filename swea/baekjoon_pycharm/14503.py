


N, M = map(int, input().split())
i, j, d = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

visited = [[0] * M for _ in range(N)]
ans = 0

while True:
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    if visited[i][j] == 0:
        visited[i][j] = 1
        ans += 1
    cnt = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if arr[ni][nj] == 0 and visited[ni][nj] == 0:
            cnt += 1
    if cnt == 0:
        ni = i - di[d]
        nj = j - dj[d]
        if arr[ni][nj] == 0:
            i, j = ni, nj
            continue
        else:
            break
    else:
        for _ in range(4):
            d -= 1
            if d < 0:
                d += 4
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj <M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                i, j = ni, nj
                break
        continue
print(ans)



