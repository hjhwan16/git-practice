# 불! / 20230914
from collections import deque
def bfs(ji, jj, maze):
    queue = deque()
    visited = [[0]*C for _ in range(R)]
    queue.append((ji, jj))
    visited[ji][jj] = 1
    while queue:
        i, j = queue.popleft()
        di = [1, -1, 0, 0]
        dj = [0, 0, 1, -1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
                if maze[ni][nj] == '.':
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return visited

def bfs_f(fire_list, maze):
    queue = deque()
    visited = [[0] * C for _ in range(R)]
    for i, j in fire_list:
        queue.append((i, j))
        visited[i][j] = 1
    while queue:
        i, j = queue.popleft()
        di = [1, -1, 0, 0]
        dj = [0, 0, 1, -1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
                if maze[ni][nj] in 'J.':
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return visited



R, C = map(int, input().split())
maze = []
for _ in range(R):
    temp = list(input())
    maze.append(temp)
# print(maze)
fire_list = []
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            ji, jj = i, j
        elif maze[i][j] == 'F':
            fire_list.append((i,j))
# print('J', ji, jj)

result_j = bfs(ji, jj, maze)
result_f = bfs_f(fire_list, maze)
# print(result_j)
# print(result_f)
min_v = 1e9
for i in range(R):
    for j in range(C):
        if i == 0 or j == 0 or i == R-1 or j == C-1:
            # print(result_j[i][j], result_f[i][j])
            if result_j[i][j] < result_f[i][j]:
                if min_v > result_j[i][j]:
                    min_v = result_j[i][j]

if min_v == 1e9:
    print('IMPOSSIBLE')
else:
    print(min_v)

'''
10 100
....................................................................................................
.......###############.......FFFF..........########.................................................
.........FFFFFFFFFFFFF#############...........................FFF..........##########....########...
.....................................................................######..................####...
.......FF...................................J.......................................................
.............................................................................................####...
......................###############################################...............................
....................................................................................................
.........FFFFFFFFFFFFF............####..........................................FFFFFF....FFFFF.....
.............................................###.######.............................................

'''