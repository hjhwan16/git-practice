# 0802.연습문제 1) 델타 연습
# 5x5 2차 배열에 25개의 숫자로 초기화
# 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
# 각 요소에 대한 절대값의 합을 구하시오.
# 25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    N = int(input()) # N * N 행렬
    # arr 입력받기
    arr = []
    tot = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # x, y 를 돌기 상/하/좌/우 순서
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            # print(arr[i][j])
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                #박스를 벗어나는 경우
                if (ni < 0) or (ni >= N) or (nj < 0) or (nj >= N):
                    continue
                #박스를 벗어나지 않는 경우
                else:
                    # 가운데 값과 절대값 차이를 구하고 더함
                    diff = arr[i][j] - arr[ni][nj]
                    if diff < 0:
                        diff *= -1
                    tot += diff
    print(f'#{tc} {tot}')