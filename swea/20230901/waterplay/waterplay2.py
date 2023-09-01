import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(queue, visited):
    while queue:
        i, j = queue.popleft()
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return visited

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []        # 모든 줄의 문자열을 모두 합쳤을 때, 적어도 하나는 W
    for _ in range(N):
        temp = list(input())
        arr.append(temp)
    # print(arr)
    ans = 0
    # 출발지들을 다 큐에 넣고 비지티드 값 1로 처리
    queue = deque()
    visited = [[-1] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0
    result = bfs(queue, visited)
    # print(result)
    for i in range(N):
        ans += sum(result[i])
    print(f'#{tc} {ans}')