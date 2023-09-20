import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        s = queue.popleft()
        for v in adj_l[s]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = visited[s] + 1
    return visited

T = 10
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 입력받는 데이터의 길이, M:시작점
    arr = list(map(int, input().split()))
    adj_l = [[] for _ in range(max(arr)+1)] # idx:from, value:to
    for i in range(N//2):
        adj_l[arr[2*i]].append(arr[2*i+1])
    # print(adj_l)
    cnt = 1
    visited = [0] * (max(arr)+1)
    result = bfs(M)
    max_cnt = max(result)
    for i in range(len(result)):
        if result[i] == max_cnt:
            ans = i
    print(f'#{tc} {ans}')
