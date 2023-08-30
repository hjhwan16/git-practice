import sys
sys.stdin = open('input.txt')

def f(i, N, arr):
    global min_v
    if i == N:
        # print(p)
        temp = 0
        for k in range(N):
            temp += arr[p[k]-1][p[k+1]-1]
        if min_v > temp:
            min_v = temp
        return
    else:
        for j in range(1, N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, arr)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 2부터 N까지 부분집합 만들고 각 경우마다 소비량 계산
    card = [i for i in range (1, N+1)]
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # print(arr)
    # print(card)
    min_v = 1e9
    used = [0] * N
    p = [1] + [0] * (N-1) + [1]
    f(1, N, arr)
    print(f'#{tc} {min_v}')