from collections import deque
# 헌내기는 친구가 필요해 bfs
def start(n, m, arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'I':
                return i, j

def bfs(si, sj, n, m, arr):
    global ans
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.popleft()
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0<= nj < m and visited[ni][nj] == 0 and arr[ni][nj] != 'X':
                queue.append((ni, nj))
                visited[ni][nj] = 1
                if arr[ni][nj] == 'P':
                    ans += 1
    return ans

n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(input())
    arr.append(temp)
si, sj = start(n, m, arr)
ans = 0
result = bfs(si, sj, n, m, arr)
'''
3 5
OOOPO
OIOOX
OOOXP

'''
if result == 0:
    print('TT')
else:
    print(result)