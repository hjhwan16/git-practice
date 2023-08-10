'''
# 1 노드의 갯수 / 엣지의 갯수
V E
7 8
# 2 인접행렬 정보 (edge, 정점이 연결되어 있는지?)
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(n, V, adj_m):
    # stack 생성
    stack = []
    # visited 생성
    visited = [0] * (V + 1)
    # 시작점 방문 표시
    visited[n] = 1
    # do[n]
    print(n)
    while True:
        # 현재 정점 n에 인접하고 미방문한 w 찾기
        for w in range(1, V+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                # 푸쉬
                stack.append(n)
                # 방문
                n = w
                print(n)
                # 방문 표시
                visited[n] = 1
                break
        else:# (갈w가 없는 경우)
            # 스택이 비어있지 않다면
            if stack:
                n = stack.pop()
            # 스택이 비었다면
            else:
                break
    return



V, E = map(int, input().split()) # V개의 정점 E개의 엣지
arr = list(map(int, input().split()))
# 인접 행렬
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[2*i], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

# 탐색
dfs(1, V, adj_m)