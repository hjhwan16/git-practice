import sys
sys.stdin = open('input.txt')


def f(i, j, t_sum):
    global min_v
    if i == N-1 and j == N-1:
        if min_v > t_sum:
            min_v = t_sum
        return
    else:
        for di, dj in [[1, 0], [0, 1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                t_sum += arr[ni][nj]
                visited[ni][nj] = 1
                f(ni, nj, t_sum)
                t_sum -= arr[ni][nj]
                visited[ni][nj] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # print(arr)
    # 결국 움직이는 건 오른쪽으로 (N-1)번 아래로 (N-1)번
    # 총 2N - 2 번 움직이는 ex N=3일 때 0 두개 1 두개
    # 따라서 0 N-1개 1 N-1개로 만들 수 있는 순열
    visited = [[0]*N for _ in range(N)]
    s_sum = arr[0][0]
    min_v = 260
    f(0, 0, s_sum)
    print(f'#{tc} {min_v}')