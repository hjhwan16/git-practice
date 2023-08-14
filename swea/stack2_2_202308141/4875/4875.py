import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    ans = 0

    # 미로 정보 받기
    for _ in range(N):
        temp = list(str(input()))
        arr.append(temp)

    #시작 위치, 끝 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    stack = []
    visited = [[0]*N for _ in range(N)]

    i, j = si, sj
    arr[i][j] = '1'

    while True:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (ni, nj) == (ei, ej):
                ans = 1
            # 박스를 벗어나지 않고 arr[ni][nj]가 0이라면 이동
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '0':
                stack.append((i, j))
                # 방문 처리
                i, j = ni, nj
                arr[i][j] = '1'
                break
        else:
            if stack:
                i, j = stack.pop()
            else:
                break

    print(f'#{tc} {ans}')
