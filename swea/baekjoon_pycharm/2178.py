# 미로탐색 bfs queue
'''
4 6
101111
101010
101011
111011

'''
from collections import deque

def bfs(si, sj, arr, n, m):
    ans = 0
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.popleft()
        di = [0, 0, 1, -1]
        dj = [-1, 1, 0, 0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))
                if ni == n - 1 and nj == m - 1:
                    ans = visited[ni][nj]
                    break
    return ans


n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(map(int, input()))
    arr.append(temp)
result = bfs(0, 0, arr, n, m)
print(result)