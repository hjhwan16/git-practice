import sys
sys.stdin = open('input.txt')

# 회문1 / 20230808 / string2

# 8*8 평면 글자판에서 제시된 길이를 가진 회문의 갯수를 구하라
#  각 칸에 들어가는 글자는 A, B, C 중 하나
# A 또한 회문
# 가로 또는 세로로 이어진 회문의 개수만 count

T = 10
for tc in range(1, T+1):
    # 찾아야 하는 회문의 길이
    N = int(input()) # pattern의 길이
    # 2차원 배열 받기
    arr = []
    for _ in range(8):
        temp = list(str(input()))
        arr.append(temp)
    # print(arr)
    # 정답 갯수
    ans = 0
    # target에서 주어진 길이 N의 패턴이 회문인지?
    M = 8 # target의 길이
    i = 0 # pattern의 idx
    # 가로 탐색
    # 길이 N인 target 만들기
    for i in range(8):
        for k in range(8-N+1):
            target = ''
            j = 0  # target의 idx
            for l in range(N):
                target += arr[i][k+l]
        # 길이가 N인 타겟이 만들어짐 이제 회문인지 체크해 주면 됨
        #     print(target)
            while j < N:
                # 일치하지 않는다면
                if target[j] != target[N-j-1]:
                    break
                j += 1
            if j == N:
                ans += 1

    # 세로 탐색
    for i in range(8):
        for k in range(8 - N + 1):
            target = ''
            j = 0  # target의 idx
            for l in range(N):
                target += arr[k+l][i]
            # 길이가 N인 타겟이 만들어짐 이제 회문인지 체크해 주면 됨
            # print(target)
            while j < N:
                # 일치하지 않는다면
                if target[j] != target[N - j - 1]:
                    break
                j += 1
            if j == N:
                ans += 1

    # 정답 프린트
    print(f'#{tc} {ans}')

