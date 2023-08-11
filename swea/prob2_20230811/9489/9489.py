import sys
sys.stdin = open('input.txt')

# 고대 유적 / 20230811

T = int(input())

for tc in range(1, T+1):
    ans = 0
    # N개의 줄, M개의 data
    N, M = map(int, input().split())
    # 2차원 배열
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    # 줄 먼저 탐색하면서 1이 나오는 순간 cnt 증가 0이 나오는 순간 멈춤 ans에 저장 후 비교하면서 최신화
    for i in range(N):
        cnt = 0
        j = 0
        while j < M:
            if arr[i][j] == 1:
                cnt += 1
                j += 1
            # 0 나오면
            else:
                # print(ans)
                if ans < cnt:
                    ans = cnt
                # cnt 최신화 후 초기화
                cnt = 0
                j += 1
        # 마지막 지점이 1인 경우도 존재하기 때문에
        if ans < cnt:
            ans = cnt

    # 열 탐색
    for j in range(M):
        cnt = 0
        i = 0
        while i < N:
            if arr[i][j] == 1:
                cnt += 1
                i += 1
            else:                # print(ans)
                if ans < cnt:
                    ans = cnt
                cnt = 0
                i += 1
        if ans < cnt:
            ans = cnt
    print(f'#{tc} {ans}')