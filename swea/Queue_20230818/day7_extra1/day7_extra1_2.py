# 비상연락망 # 인접 행렬
import sys
sys.stdin = open('input.txt')

def bfs(S, adj_m):
    max_v = 0
    max_idx = 0
    visited = [0] * 101
    queue = []
    queue.append(S)
    visited[S] = 1
    while queue:
        t = queue.pop(0)
        for w in range(101):
            if not visited[i] and adj_m[t][] == 1:
                queue.append(i)
                visited[i] = visited[t] + 1
                print(i)
    # visited 에서 최댓값 idx 찾기
    # for i in range(101):
    #     if visited[i] >= visited[max_idx]:
    #         max_idx = i

    return max_idx


T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())    # N: 입력받는 데이터, S: 시작점
    arr = list(map(int, input().split()))
    # 인접 행렬 ㄱㄱ
    adj_m = [[0] * 101 for _ in range(101)] # 인접 리스트에 오름차순으로 정렬 되면 바로 될 듯?
    for i in range(N//2):
        v1, v2 = arr[2*i], arr[2*i + 1]
        adj_m[v1][v2] = 1
    ans = bfs(S, adj_m)
    print(f'#{tc} {ans}')
