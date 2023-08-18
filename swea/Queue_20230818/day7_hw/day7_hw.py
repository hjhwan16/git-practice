# 미로1 / 20230818
import sys
sys.stdin = open('input.txt')

def start(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(si, sj, N):
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.pop(0)
        di = [0, 0, -1, 1]
        dj = [-1, 1, 0, 0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if maze[ni][nj] == 3:
                    return 1
    return 0





T = 10
N = 16
for tc in range(1, T+1):
    c = int(input())
    maze = []
    for _ in range(N):
        temp = list(map(int, input()))
        maze.append(temp)
    si, sj = start(maze)    # 시작점 찾기
    ans = bfs(si, sj, N)    # 도착할 수 있는지
    print(f'#{tc} {ans}')