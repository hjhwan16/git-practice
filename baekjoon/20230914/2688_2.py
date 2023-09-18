import sys
input = sys.stdin.readline

def dfs(s):
    route = set()
    stack = []
    visited = [0] * (N+1)
    visited[s] = -1
    while True:
        for v in adj_l[s]:
            if visited[v] != 1:
                stack.append(s)
                s = v
                visited[s] = 1
                route.add(s)
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    return route

N = int(input())
adj_l = [[] for _ in range (N+1)]
for i in range(N):
    num = int(input())
    adj_l[i+1].append(num)

# print(adj_l)
ans = set()
for i in range(1, N+1):
    result = dfs(i)
    # print(i, result)
    if i in result:
        ans = ans | result

ans = list(ans)
l = len(ans)
print(l)
ans.sort()
# print(ans)
for i in ans:
    print(i)