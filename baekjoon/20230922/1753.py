# 최단 경로 / 다익스트라
import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())    # 시작점
graph = [[] for _ in range (V+1)]
# print(graph)
for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f].append((t, w))

INF = 1e9
distance = [INF] * (V+1)

def dijkstra(start):
    # 시작조건 초기화
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 지점 확인
        dist, now = heapq.heappop(pq)

        # 전처리
        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


dijkstra(K)

for i in range(1, V+1):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])