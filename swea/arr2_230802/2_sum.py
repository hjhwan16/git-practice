# 100x100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램
# 10개의 테스트 케이스가 주어짐
# 배열의 크기는 100x100으로 동일
# 동일한 최댓값이 있을 경우 하나의 값만을 출력
import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input()) # 테스트 케이스 번호
    ans = 0
    # 2차원 배열 입력받기
    arr = []
    for _ in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)

    # 행 우선 탐색 후 더하기
    for i in range(100):
        tot_temp = 0
        # 각 행의 합 구하기
        for j in range(100):
            tot_temp += arr[i][j]
        # 각 행이 최댓값 인지 확인 후 반환하기
        if ans < tot_temp:
            ans = tot_temp

    # 열 우선 탐색 후 더하기
    for j in range(100):
        tot_temp = 0
        # 각 열의 합 구하기
        for i in range(100):
            tot_temp += arr[i][j]
        # 최댓값 인지 확인 후 변환하기
        if ans < tot_temp:
            ans = tot_temp

    # 대각선 탐색 후 더하기 좌상 우하
    tot_temp = 0
    for i in range(100):
        tot_temp += arr[i][i]
    # 최댓값 인지 확인 후 변환하기
    if ans < tot_temp:
        ans = tot_temp

    # 대각선 탐색 후 더하기 우상 좌하
    tot_temp = 0
    for i in range(100):
        tot_temp += arr[i][99-i]
    # 최댓값 인지 확인 후 변환하기
    if ans < tot_temp:
        ans = tot_temp

    print(f'#{N} {ans}')