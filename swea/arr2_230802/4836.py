# 색칠하기
# 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 함.
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어짐
# 칠이 끝난 후 색이 겹쳐 보라색이 된 칸의 갯수를 구하시오.
# x1, y1, x2, y2, color / color 1: 빨강, color 2:파랑

import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    # 빈 격자 만들기(10 by 10)
    arr = [[0]*10 for _ in range(10)]
    ans = 0
    N = int(input()) # 칠할 영역의 갯수
    # 1번 칠할 때 마다 빈 격자에 빨강 -> 1을 더해주고 파랑 -> 2를 더해줌

    # 위 두 케이스를 만족할 때 마다 ans += 1
    for k in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                # 빨강색을 칠할 때 해당 격자가 0이 아닌 짝수라면 -> 해당 격자는 보라색이 됨
                if color == 1:
                    if (arr[i][j] != 0) and (arr[i][j] % 2 == 0):
                        arr[i][j] += 1
                        ans += 1
                    else:
                        arr[i][j] += 1
                # 파랑색을 칠할 때 해당 격자가 홀수라면 -> 해당 격자는 보라색이 됨
                elif color == 2:
                    if arr[i][j] % 2:
                        arr[i][j] += 2
                        ans += 1
                    else:
                        arr[i][j] += 2
    print(f'#{tc} {ans}')