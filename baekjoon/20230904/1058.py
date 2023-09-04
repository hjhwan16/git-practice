# BFS를 이용해 두번 움직였을 때 visited list가 1이 되는 갯수를 탐색
'''
3
NYY
YNY
YYN

'''
from collections import deque
N = int(input())
arr = [[0] * (N+1)]
for _ in range(N):
    temp = [0] + list(input())
    arr.append(temp)
# print(arr)
adj_m = [[0] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if arr[i][j] == 'Y':
            adj_m[i][j] = 1
        else:
            adj_m[i][j] = 0
# print(adj_m)

# bfs 구현 bfs는 큐
def bfs(s, N):  #s: 시작점
    visited = [0] * (N+1)
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.popleft()
        for v in range(1, N+1):
            if visited[v] == 0 and adj_m[t][v] == 1:
                visited[v] = visited[t] + 1
                queue.append(v)
    return visited
max_v = 0
for i in range(1, N+1):
    result = bfs(i, N)
    # print(result)
    temp = 0
    for k in result:
        if k <= 3 and 1 < k:
            temp += 1
    # print(temp)
    if max_v < temp:
        max_v = temp
print(max_v)