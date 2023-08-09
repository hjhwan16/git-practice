import sys
sys.stdin = open('input.txt')
# 이동방향 순서
#     우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 모두 0인 N by N 배열 만들기
    arr = [[0]*N for _ in range(N)]

    count = 1 # 기록 변수
    x, y = 0, 0 # 시작좌표
    dir = 0 # 방향 변수
    arr[x][y] = count # 시작1

    # 반복 시작
    while count < N**2:
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 다음 자리가 박스안에 들어오고 0이라면?
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            count += 1
            # 자리에 conut 할당
            arr[nx][ny] = count
            # 위치 갱신
            x, y = nx, ny
        # 아니면?
        else:
            # 달팽이의 방향 전환은 정해져 있음
            dir += 1
            if dir >= 4:
                dir = 0

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()