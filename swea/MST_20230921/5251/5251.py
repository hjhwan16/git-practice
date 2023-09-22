import sys
sys.stdin = open('input.txt')

# 다익스트라 알고리즘을 활용한 풀이

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())    # 노드의 수:N, 간선의 수:E
    # 인접리스트
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    # 누적거리
    INF = 1e9
    distance = [INF] * (N+1)
    # print(distance)
    def dijkstra(start):
        pq = []
        # 누적거리 초기화 후 우선순위 큐에 넣어주기
        pq.append((0, start))
        distance[start] = 0

        while pq:
            # 현재 누적거리가 제일 짧은 노드와 정보 꺼내기
            pq = sorted(pq, key=lambda x:x[1])
            dist, now = pq.pop()
            # 이미 방문했거나, 누적거리가 짧으면 pass
            if distance[now] < dist:
                continue
            # 인접노드 정보 꺼내기
            for next in graph[now]:
                next_node = next[0]
                cost = next[1]

                # 누적거리 만들어 주기
                new_cost = dist + cost

                # 기존값보다 크다면 pass
                if distance[next_node] < new_cost:
                    continue

                # 아니면 추가
                distance[next_node] = new_cost
                pq.append((new_cost, next_node))



    # 0부터 N까지 도착하는 경우
    dijkstra(0)
    # print(distance)
    result = distance[N]
    print(f'#{tc} {result}')