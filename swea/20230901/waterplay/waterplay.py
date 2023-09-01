import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(i, j):
    flag = True
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    queue.append((i, j))     # 시작 점 큐에 추가
    visited[i][j] = 1        # 시작 접 방문 처리
    while queue:
        i, j = queue.popleft()
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))
                if arr[ni][nj] == 'W' and flag:
                    flag = False
                    return visited[ni][nj] - 1


# 땅인 칸에서 시작해서 물로 갈 수 있는 최소거리의 합
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []        # 모든 줄의 문자열을 모두 합쳤을 때, 적어도 하나는 W
    for _ in range(N):
        temp = list(input())
        arr.append(temp)
    # print(arr)
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':    # 땅이라면 탐색 후 최단 거리 더하기
                result = bfs(i, j)  # 최단거리 탐색 함수
                ans += result

    print(f'#{tc} {ans}')