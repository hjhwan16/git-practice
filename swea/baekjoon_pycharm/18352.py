# N개의 도시와 M개의 단방향 도로
# 최단거리가 K인 도시번호를 출력, 시작점 X
import sys
input = sys.stdin.readline

def bfs(N, X):
    queue = []
    visited = [0] * (N+1)
    queue.append(X)
    visited[X] = 1
    while queue:
        t = queue.pop(0)
        for w in range(1, N+1):
            if visited[w] == 0 and t in adj_dict.keys() and w in adj_dict[t]:
                queue.append(w)
                visited[w] = visited[t] + 1
    return visited

N, M, K, X = map(int, input().split())
adj_dict = {}
for _ in range(M):
    v1, v2 = map(int, input().split())
    if v1 not in adj_dict.keys():
        adj_dict[v1] = [v2]
    else:
        adj_dict[v1].append(v2)
result = bfs(N, X)
ans = []
for i in range(1, N+1):
    if result[i]-1 == K:
        ans.append(i)

if ans:
    for i in ans:
        print(i)
else:
    print(-1)
