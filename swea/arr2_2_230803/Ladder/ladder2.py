# 20230803 / HW / Ladder1

import sys
sys.stdin = open('input.txt')

# 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정

# 어느 사다리를 고르면 X표시에 도착하는지 구하시오.

# 시작점 기준으로 아래의 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향전환

# 방향 전환 이후엔 다시 아래 방향으로만 이동, 바닥에 도착하면 멈춤

# 100 x 100 크기의 사다리가 2차원 배열로 주어짐

# 도착지점은 2로 표시됨 2로 도착하는 출발점 X를 구하시오.

for tc in range(1, 11):
    N = int(input())
    # 2차원 배열 만들기
    arr = []
    for _ in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # 도착지 찾기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                start_i = i
                start_j = j
    # print(start_i, start_j)

    # 도착지에서 거꾸로 올라가면서 출발지 찾기
    while True:
        if start_i == 0:
            ans = start_j
            break
        #좌탐색
        if start_j > 0 and arr[start_i][start_j - 1] == 1:
            while start_j > 0 and arr[start_i][start_j - 1] == 1:
                start_j -= 1
            start_i -= 1
        #우탐색
        elif start_j < 99 and arr[start_i][start_j + 1] == 1:
            while start_j < 99 and arr[start_i][start_j + 1] == 1:
                start_j += 1
            start_i -= 1
        #나머지
        else:
            start_i -= 1

    print(f'#{tc} {ans}')