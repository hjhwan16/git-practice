import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 2차원 배열 받기
    arr = []
    for _ in range(N):
        temp = list(input())
        arr.append(temp)
    ans = ''
    # 길이 M인 걸로
    # 가로 회문 판독
    for i in range(N):
        for j in range(N-M+1):
            # temp1이 0으로 유지된 경우 그 문항은 회문.
            temp1 = 1
            for k in range(M//2):
                # 가로 회문 판독
                if arr[i][j+k] != arr[i][j+M-k-1]:
                    temp1 = 0
                    break
            # 회문인 경우 ans 프린트
            if temp1 == 1:
                for l in range(M):
                    ans += arr[i][j+l]

    # 세로 회문 판독
    for j in range(N):
        for i in range(N-M+1):
            # temp2가 0으로 유지되면 회문 아니면 회문 x
            temp2 = 1
            for k in range(M//2):
                if arr[i+k][j] != arr[i+M-k-1][j]:
                    temp2 = 0
                    break
            if temp2 == 1:
                for l in range(M):
                    ans += arr[i+l][j]

    print(f'#{tc} {ans}')