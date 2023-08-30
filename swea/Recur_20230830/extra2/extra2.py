import sys
sys.stdin = open('input.txt')
# 회사에서 출발해 N명의 고객을 모두 방문 후 집으로 돌아오는 경로 중 가장 짧은 것
def f(i, N):
    global min_v
    if i == N:
        total = 0
        for i in range(N):
            if i == 0:
                temp_x = abs(ci - custom_loc[p[i]][0])
                temp_y = abs(cj - custom_loc[p[i]][1])
            else:
                temp_x = abs(custom_loc[p[i-1]][0] - custom_loc[p[i]][0])
                temp_y = abs(custom_loc[p[i-1]][1] - custom_loc[p[i]][1])
            total += temp_x + temp_y
        temp_x = abs(hi - custom_loc[p[N-1]][0])
        temp_y = abs(hj - custom_loc[p[N-1]][1])
        total += temp_x + temp_y
        if min_v > total:
            min_v = total

        #회사에서 출발해서 집까지

        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = custom_idc[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 고객의 수
    arr = list(map(int, input().split()))
    ci, cj = arr[0], arr[1]     # 회사 좌표
    hi, hj = arr[2], arr[3]     # 집 좌표
    custom_idc = [i for i in range(N)]
    custom_loc = []
    min_v = 1e19
    for i in range(2, N+2):
        custom_loc.append([arr[2*i], arr[2*i + 1]])
    # print(ci,cj)
    # print(hi,hj)
    # print(custom_idc)
    # print(custom_loc)
    used = [0] * N
    p = [0] * N
    f(0, N)
    print(f'#{tc} {min_v}')