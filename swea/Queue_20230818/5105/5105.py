# 미로의 거리 / 20230818
import sys
sys.stdin = open('input.txt')

# 시작점 찾는 함수
def start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

# visited 있이
def bfs(si, sj, N):
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        i, j = queue.pop(0) # 뽑아서
        di = [0, 0, -1, 1]
        dj = [-1, 1, 0, 0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 새로운 지점이 범위 안에 있고 0이라면~
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                if arr[ni][nj] == 3:
                    return visited[ni][nj] - 2
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(map(int, input()))
        arr.append(temp)
    # 시작점 찾기
    si, sj = start(arr)

    # 거리 반환하는 함수 bfs
    ans = bfs(si, sj, N)
    print(f'#{tc} {ans}')