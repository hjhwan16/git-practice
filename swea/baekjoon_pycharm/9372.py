import sys
input = sys.stdin.readline

def dfs(s,N,adj_dict):
    ans = -1
    stack = []
    visited = [0] * (N+1)
    visited[s] = 1

    while True:
        for w in adj_l[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w
                visited[s] = 1
                ans += 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

    return ans


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 국가의 수, M: 비행기의 종류
    adj_l = [[0] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)

    result = dfs(1, N, adj_l)
    print(result)

'''
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5

'''
