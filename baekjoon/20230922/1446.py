# 지름길 / 다익스트라
import heapq

N, D = map(int, input().split())    #N: 지름길의 갯수 / D: 고속도로의 길이
graph = {}
for _ in range(N):
    f, t, w = map(int, input().split())
    # 안에 있다면 value에 추가
    if f in graph.keys():
        graph[f].append([t, w])
    # 없다면 2중 리스트로 추가
    else:
        graph[f] = [[t, w]]
# print(graph)
# print(list(graph.keys()))
# L = len(graph.keys())
# print(L)

INF = 1e9
distance = [INF] * (D+10)

def dijkstra(start):
    # 우선순위 큐
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서 누적거리가 가장 짧은 노드에 대한 정보
        dist, now = heapq.heappop(pq)
        if now > D:
            continue
        if distance[now] < dist:
            continue

        # 지름길이 있다면?
        if now in graph.keys():
            for next in graph[now]:
                next_node = next[0]
                cost = next[1]

                # 누적거리 계산
                new_cost = dist + cost
                if next_node > D:
                    continue

                # 누적거리가 기존값 보다 크다면 pass
                if distance[next_node] < new_cost:
                    continue

                # 아니면? 추가하기
                # print('추', next_node, new_cost)

                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

        # 지름길이 없다면?
        # 누적거리
        # print('없')
        new_cost = dist + 1
        next_node = now + 1
        if next_node > D:
            continue
        # 기존값 보다 크다면?
        # print(next_node)
        if distance[next_node] <= new_cost:
            continue
        # 아니면? 추가하기
        # print('추')
        distance[next_node] = new_cost
        heapq.heappush(pq, (new_cost, next_node))
        if next_node == D:
            return


dijkstra(0)
print(distance[D])