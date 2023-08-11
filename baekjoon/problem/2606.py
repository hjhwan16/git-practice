# 바이러스 dfs / 20230801

# 컴퓨터 -> 노드의 수
V = int(input())
# 엣지의 수
E = int(input())

adj_m = [[0]*(V + 1) for _ in range(V + 1)]

# 입력받고 인접행렬 만들기
for i in range(E):
    v1, v2 = map(int, input().split())
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

#dfs 알고리즘 만들기
def dfs(s, v, adj_m):
    stack = []
    visited = [0] * (v + 1)
    visited[s] = 1
    while True:
        for w in range(1, v+1):
            if adj_m[s][w] == 1 and visited[w] == 0:
                stack.append(s)
                s = w
                visited[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    return visited



result = dfs(1, V, adj_m)
ans = 0
for i in result:
    if i == 1:
        ans += 1

# 1은 제외
print(ans-1)
