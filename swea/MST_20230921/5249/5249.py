import sys
sys.stdin = open('input.txt')

import heapq

def prim(start):
    heap = []
    MST = [0] * (V+1)
    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))
    sum_weight = 0

    while heap:
        # 가장 작은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드러면 pass
        if MST[v] == 1:
            continue

        # 아니면 방분!
        MST[v] = 1
        sum_weight += weight

        # 인접 노드 체크
        for next in range(V+1):
            # 연결되어있지 않거나 방문한 노드는 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            # 아니면 추가!
            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight

# MST
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 행렬 만들기
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        f, t, w = map(int, input().split())
        graph[f][t] = w
        graph[t][f] = w
    # print(graph)
    ans = prim(0)
    print(f'#{tc} {ans}')
