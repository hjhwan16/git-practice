from collections import deque
# 숨바꼭질3 / 20230912

dp = [0]*100000
N, K = map(int, input().split()) #N이 시작 k가 도착

def bfs(N, K):
    visited = [-1]*100001
    queue = deque()
    queue.append(N)
    visited[N] = 0

    while queue:
        t = queue.popleft()
        for s in [t-1, t+1]:
            if 0 <= s < 100001 and visited[s] == -1:
                queue.append(s)
                if s == 2*t:
                    visited[s] = visited[t]
                else:
                    visited[s] = visited[t] + 1
                # print(s, visited[s])
                if s == K:
                    return visited[K]

if N == K:
    print(0)
else:
    result = bfs(N, K)
    print(result)