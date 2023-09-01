# 토마토 / 20230901
from collections import deque
M, N = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
queue = deque()
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i,j))
max_v = 0
while queue:
    i, j = queue.popleft()
    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
            queue.append((ni, nj))
            arr[ni][nj] = arr[i][j] + 1

flag = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = False
            break
        else:
            if max_v < arr[i][j]:
                max_v = arr[i][j]

if not flag:
    print(-1)
else:
    print(max_v-1)

