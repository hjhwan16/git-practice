import sys
sys.stdin = open('input.txt')

def f(si, sj):
    max_visit = 1
    visited[si][sj] = 1
    queue = []
    queue.append((si, sj))
    while queue:
        si, sj = queue.pop(0)
        max_visit = max(max_visit, visited[si][sj])
        di = [0, 0, -1, 1]
        dj = [1, -1, 0, 0]
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == arr[si][sj] + 1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[si][sj] + 1

    return max_visit


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(map(int,input().split()))
        arr.append(temp)

    room_num = N*N+1
    room_cnt_max = 0

    for num in range(1, N*N+1):
        visited = [[0]*N for _ in range(N)]
        si, sj = (num - 1) // N, (num - 1) % N
        room_cnt = f(si, sj)
        if room_cnt_max < room_cnt:
            room_cnt_max = room_cnt
            room_num = arr[si][sj]
        elif room_cnt_max == room_cnt:
            room_num = min(room_num, arr[si][sj])

    print(f'#{tc} {room_num} {room_cnt_max}')