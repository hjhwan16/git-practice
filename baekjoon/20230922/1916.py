# 최소비용 / 다익스트라
# A 부터 B 도시 까지 가는 최소 비용

import heapq
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
# 인접 리스트 받기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    f, t, w = map(int, input().split())
    graph[f].append((t, w))
# print(graph)

s, g = map(int, input().split())

# 초기 누적거리
maxsize = 1e9
distance = [maxsize] * (N+1)

def dijkstra(start, goal):
    # 초기 설정
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서 누적거리가 짧은 노드에 대한 정보 추출
        dist, now = heapq.heappop(pq)

        # 전처리
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            # print(next_node, cost)
            #누적거리
            new_cost = dist + cost

            # 전처리 같아지는 경우도 동일한 경우이기 때문에 skip 해줘야 한다.
            if distance[next_node] <= new_cost:
                continue
            # 아니면 추가
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
            # print(distance)

if s == g:
    print(0)
else:
    dijkstra(s, g)
    # print(distance)
    print(distance[g])


