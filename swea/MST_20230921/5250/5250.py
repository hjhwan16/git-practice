# 델타 / 다익스트라
import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    INF = 1e9
    distance = [[INF] * N for _ in range(N)]

    def dijkstra(si, sj):
        # 우선순위 큐
        pq = []
        # 출발점 초기화
        heapq.heappush(pq, (0, si, sj))
        distance[si][sj] = 0

        while pq:
            # 현재 시점에서 누적거리가 가장 짧은 노드에 대한 정보 꺼내기
            dist, now_i, now_j = heapq.heappop(pq)

            # 이미 방문했고 누적거리가 더 짧다면 pass
            if distance[now_i][now_j] < dist:
                continue

            # 인접 노드를 델타로 확인
            di = [0, 0, 1, -1]
            dj = [-1, 1, 0, 0]
            for k in range(4):
                next_i = now_i + di[k]
                next_j = now_j + dj[k]
                # 밖에 나가면 pass
                if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N:
                    continue
                # 누적거리
                # 올라가는 경우
                if graph[next_i][next_j] > graph[now_i][now_j]:
                    new_cost = dist + 1 + graph[next_i][next_j] - graph[now_i][now_j]
                else:
                    new_cost = dist + 1

                # 누적거리가 기존보다 크다면?
                if distance[next_i][next_j] <= new_cost:
                    continue

                # 아니면 추가해주기
                distance[next_i][next_j] = new_cost
                heapq.heappush(pq, (new_cost, next_i, next_j))


    dijkstra(0,0)
    result = distance[N-1][N-1]
    print(f'#{tc} {result}')
