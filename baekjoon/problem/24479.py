# DFS / 20230810

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(s, v, adj_m):
    # 방문순서
    route = []
    # stack 생성
    stack = []
    # visited 생성
    visited = [0] * (v+1)
    # 시작점 방문 처리
    visited[s] = 1
    route.append(s)
    # 돌기
    while True:
        for w in range(1, v+1):
            if adj_m[s][w] == 1 and visited[w] == 0:
                # 스택에 넣고
                stack.append(s)
                # 방문 처리
                s = w
                visited[s] = 1
                route.append(s)
                break
        # 아닌 경우
        else:
            # 스택이 빈 경우가 아닐 때
            if stack:
                s = stack.pop()
            else:
                break
    return route


V, E, S = map(int, input().split())
# E 개의 간선 정보가 주어짐
adj_m = [[0] * (V + 1) for _ in range(V + 1)]
# 양방향 인접행렬 만들기
for i in range(E):
    v1, v2 = map(int, input().split())
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

# 정점 방문 순서 리스트 반환
result = dfs(S, V, adj_m)
# print(result)
for i in range(1, V+1):
    if i in result:
        print(result.index(i) + 1)
    else:
        print(0)

## 메모리 초과로 문제가 안풀림 ㅆㅃ