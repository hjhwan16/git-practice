# extra / 1979 / 어디에 단어가 들어갈 수 있을까
# N x N 크기의 단어 퍼즐을 만들려고 함.
# 흰색에 글자가 들어갈 수 있고 흰색이 1 검은색이 0
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하시오.
import sys
sys.stdin = open('input.txt')
# N은 5이상 15이하의 정수
# K는 2이상 N이하의 정수

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    # 2차원 배열 입력받기
    arr = []
    for row in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # 연속된 1의 합이 K가 되는 경우를 찾음
    # 행 우선 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            # 검은색이면 cnt가 K값과 동일한지 확인 한 뒤 cnt값 초기화
            if arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1
        # 마지막까지 흰생일 경우 cnt 값 체크해주기
        if cnt == K:
            ans += 1
    # 열 탐색
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            ans += 1

    print(f'#{tc} {ans}')
