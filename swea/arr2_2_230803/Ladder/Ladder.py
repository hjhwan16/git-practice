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
    # 정답 초기화
    ans = 0

    for j in range(100):
        if arr[0][j] == 1:
            # 시작점 설정
            ni = 1
            nj = 0 + j
            # 한 칸씩 내려가면서 탐색
            while True:
                # print(ni, nj)
                if ni == 99:
                    if arr[ni][nj] == 2:
                        ans = j
                    break
                # 오른쪽 탐색
                if nj < 99 and arr[ni][nj + 1] == 1:
                    while nj < 99 and arr[ni][nj + 1] == 1:
                        nj += 1
                    ni += 1

                # 왼쪽 탐색
                elif 0 < nj and arr[ni][nj - 1] == 1:
                    while 0 < nj and arr[ni][nj - 1] == 1:
                        nj -= 1
                    ni += 1
                # 아래로
                else:
                    ni += 1
    print(f'#{tc} {ans}')




'''
i = 1
            print(i, j)
            while True:
                print(i, j)
                # 벗어나는 경우
                if j+1 >= 100 or j-1 < 0 or i+1 >= 100:
                    continue
                # 오른쪽(0, +1)과 1인 경우 오른쪽으로 이동
                elif arr[i][j+1] == 1:
                    j = j+1
                    print(i, j)
                # 왼쪽이(0, -1) 1인 경우 왼쪽으로 이동
                elif arr[i][j-1] == 1:
                    j = j - 1
                    print(i, j)
                elif arr[i+1][j] == 1:
                    i = i + 1
                    print(i, j)
                    if i == 99:
                        break
                elif arr[i+1][j] == 2:
                    ans = i+1
                    print(i, j)
                    break
                else:
                    print(i, j)
    
'''