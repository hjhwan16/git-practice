from collections import deque
# 출발지점이 여러개인 BFS
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

queue = deque()
visited = [[-1]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 0

max_v = -1

while queue:
    i, j = queue.popleft()
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
            queue.append((ni, nj))
            visited[ni][nj] = visited[i][j] + 1
            if max_v < visited[ni][nj]:
                max_v = visited[ni][nj]

print(max_v)