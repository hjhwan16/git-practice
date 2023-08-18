# 비상연락망
import sys
sys.stdin = open('input.txt')

def bfs(S, adj_l):
    max_v = 0
    max_idx = 0
    visited = [0] * 101
    queue = []
    queue.append(S)
    visited[S] = 1
    while queue:
        t = queue.pop(0)
        for i in adj_l[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
                print(i)
    # visited 에서 최댓값 idx 찾기
    for i in range(101):
        if visited[i] >= visited[max_idx]:
            max_idx = i

    return max_idx


T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())    # N: 입력받는 데이터, S: 시작점
    arr = list(map(int, input().split()))
    # 인접 리스트 ㄱㄱ
    adj_l = [set() for _ in range(100 + 1)] # 인접 리스트에 오름차순으로 정렬 되면 바로 될 듯?
    for i in range(N//2):
        v1, v2 = arr[2*i], arr[2*i + 1]
        adj_l[v1].add(v2)
    ans = bfs(S, adj_l)
    print(f'#{tc} {ans}')
