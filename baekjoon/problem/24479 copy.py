# DFS / 20230810
count = 0
import sys
input = sys.stdin.readline

def dfs(s, graph):
    # 방문순서
    global count
    count += 1
    route = []
    # stack 생성
    stack = []
    # visited 생성
    # 시작점 방문 처리
    visited[s] = count
    route.append(s)
    # 돌기
    while True:
        for w in graph[s]:
            if visited[w] == 0:
                # 스택에 넣고
                stack.append(s)
                # 방문 처리
                s = w
                count += 1
                visited[s] = count
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
# 양방향 인접리스트 만들기
visited = [0] * (V+1)
graph = {}
for i in range(E):
    v1, v2 = map(int, input().split())
    if v1 not in graph.keys():
        graph[v1] = set([v2])
    else:
        graph[v1].add(v2)
    # 양방향이기 때문에
    if v2 not in graph.keys():
        graph[v2] = set([v1])
    else:
        graph[v2].add(v1)

# 정점 방문 순서 리스트 반환

result = dfs(S, graph)
# print(result)
for i in range(1, V+1):
    print(visited[i])

    ## 메모리 초과로 문제가 안풀림 ㅆㅃ
    ## 시간초과 씨ㅃ라