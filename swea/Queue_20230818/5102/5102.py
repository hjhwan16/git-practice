# 노드의 거리 / 20230818
import sys
sys.stdin = open('input.txt')

# 주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지?
def bfs(S, G, V):
    visited = [0] * (V+1)   # visited 배열 생성
    queue = []              # queue 생성
    queue.append(S)         # 시작점 큐에 추가
    visited[S] = 1          # 시작점 방문 처리
    while queue:            # 큐가 빌 때까지
        t = queue.pop(0)
        for i in adj_l[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
                if i == G:  # G에 도달한다면
                    return visited[i]-1 # 경로 - 1 반환 why? 시작이 1이라

    # 못만나면
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접행렬
    adj_l = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)

    # 출발, 도착지
    S, G = map(int, input().split())
    ans = 0
    ans = bfs(S, G, V)
    print(f'#{tc} {ans}')