import sys

input = sys.stdin.readline
# print = sys.stdout.write

# dfs
V, E, S = map(int, input().split())
# 인접 리스트: dict
adj_d = {}
for _ in range(E):
    v1, v2 = map(int, input().split())
    if v1 not in adj_d.keys():
        adj_d[v1] = [v2]
    else:
        adj_d[v1].append(v2)
    if v2 not in adj_d.keys():
        adj_d[v2] = [v1]
    else:
        adj_d[v2].append(v1)


def dfs(V, S, adj_d):
    stack = []
    visited = [0] * (V + 1)
    cnt = 1
    visited[S] = cnt
    while True:
        adj_d[S].sort(reverse = True)
        for w in adj_d[S]:
            if visited[w] == 0:
                stack.append(S)
                S = w
                cnt += 1
                visited[S] = cnt
                break
        else:
            if stack:
                S = stack.pop()
            else:
                break
    return visited


if S not in adj_d.keys():
    result = [0] * (V + 1)
    result[S] = 1
    for i in range(1, V + 1):
        print(result[i])
elif len(adj_d[S]) == (V - 1):
    result = [0] * (V + 1)
    cnt = 1
    result[S] = cnt
    adj_d[S].sort(reverse = True)
    for i in adj_d[S]:
        cnt += 1
        result[i] = cnt
    for i in range(1, V + 1):
        print(result[i])
else:
    result = dfs(V, S, adj_d)
    for i in range(1, V + 1):
        print(result[i])
