# extra / 1974 / 스도쿠 검증
# 가로 9칸 세로 9칸의 스도쿠 1부터 9까지의 숫자를 채워 넣음
# 같은 줄에 1부터 9까지
# 같은 열에 1부터 9까지
# 격자 안에 1부터 9까지
# 조건 만족 1을 출력 만족 x 0을 출력
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cnt = 0 #cnt가 0이어야 정답
    # 2차원 배열 입력받기
    arr = []

    for row in range(9):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # 행검증
    for i in range(9):
        temp_set = set()
        for j in range(9):
            temp_set.add(arr[i][j])
        if len(temp_set) == 9:
            cnt += 0
        else:
            cnt += 1
    # 열 검증
    for j in range(9):
        temp_set = set()
        for i in range(9):
            temp_set.add(arr[i][j])
        if len(temp_set) == 9:
            cnt += 0
        else:
            cnt += 1
    # 격자 검증
    for i in range(0, 9, 3): #0 3 6
        for j in range(0, 9, 3):
            temp_set = set()
            for k in range(3):
                for l in range(3):
                    temp_set.add(arr[i+k][j+l])
            if len(temp_set) == 9:
                cnt += 0
            else:
                cnt += 1
    if cnt == 0:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
