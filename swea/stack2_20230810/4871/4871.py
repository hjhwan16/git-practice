import sys
sys.stdin = open('input.txt')

# V개의 노드 E개의 엣지
# 특정한 두 개의 노드에 경로가 존재하는지를 확인
# 두 개의 노드에 대해 경로가 있으면 1 없으면 0을 출력

# S에서 G가 연결 되어 있는지 V 노드의 갯수
def dfs(s, g, v, adj_m):
    stack = [] # stack 만들기
    visited = [0] * (v + 1)
    # 시작점 방문 처리
    visited[s] = 1
    ans = 0
    # print(n)
    while True:
        # 인접하고 방문하지 않은 w 찾기
        for w in range(1, v+1):
            if (adj_m[s][w] == 1) and (visited[w] == 0):
                # stack에 push
                stack.append(s)
                # 방문
                s = w
                visited[s] = 1
                # print(n)
                break
        else:
            # 스택이 비어있지 않은 경우
            if stack:
                s = stack.pop()
            # 스택이 비었어?
            else:
                break
    if visited[g]:
        ans = 1
    return ans


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접행렬 만들기
    adj_m = [[0]*(V+1) for _ in range(V+1)]

    # 연결 정보
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_m[v1][v2] = 1
    # 확인할 노드
    S, G = map(int, input().split())
    # 연결되어 있으면 1, 아니면 0
    result = dfs(S, G, V, adj_m)

    print(f'#{tc} {result}')