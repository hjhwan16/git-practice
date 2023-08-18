'''
5 5 1
1 4
1 2
2 3
2 4
3 4

'''
def bfs(V, E, S):
    visited = [0] * (V+1)
    cnt = 1
    visited[S] = cnt
    queue = []
    queue.append(S)
    while queue:
        t = queue.pop(0)
        adj_l[t].sort(reverse=True)
        for i in adj_l[t]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                queue.append(i)
    return visited

V, E, S = map(int, input().split())
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = map(int, input().split())
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

result = bfs(V, E, S)
for i in range(1, V+1):
    print(result[i])
