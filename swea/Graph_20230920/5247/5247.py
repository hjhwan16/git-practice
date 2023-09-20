import sys
sys.stdin = open('input.txt')
from collections import deque
def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    visited[N] = 1
    while queue:
        s, cnt = queue.popleft()

        # print(s, cnt)
        for k in range(4):
            if k == 0:
                ns = s + 1
            elif k == 1:
                ns = s - 1
            elif k == 2:
                ns = s * 2
            else:
                ns = s - 10
            if ns == M:
                # print(N, cnt+1)
                return cnt + 1
            if ns <= 1000000 and visited[ns] == 0:
                queue.append((ns, cnt+1))
                visited[ns] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N을 M으로 만들어야 함.
    visited = [0] * 1000001
    result = bfs(N, M)
    print(f'#{tc} {result}')