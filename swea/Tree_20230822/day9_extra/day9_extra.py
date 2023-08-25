import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 한 변의 길이 / M: 돌을 놓는 횟수
    board = [[0]*N for _ in range(N)]

    # 초기 돌 배치
    board[N//2 - 1][N//2 - 1] = 2
    board[N//2 - 1][N//2] = 1
    board[N//2][N//2 - 1] = 1
    board[N//2][N//2] = 2

    for _ in range(M):
        arr = list(map(int, input().split()))
        j = arr[0] - 1
        i = arr[1] - 1
        # arr[j, i, c] j는 열 i가 행 c:1이 흑돌, 2가 백돌
        # 배치 위치에 돌 배치하고 delta 탐색해서 바뀔수 있는 돌 바꾸기.
        board[i][j] = arr[2]
        di = [0, 0, 1, -1, 1, 1, -1, -1]
        dj = [-1, 1, 0, 0, 1, -1, 1, -1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            stack = []
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] != 0 and board[ni][nj] != board[i][j]:
                    while True:
                        stack.append((ni, nj))
                        ni = ni + di[k]
                        nj = nj + dj[k]
                        # 0이 아니고 다르다면 stack에 qppend
                        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 0 and board[ni][nj] != board[i][j]:
                            continue
                            # 0이 아니고 동일하다면 stack 비우고  break
                        elif 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 0  and board[ni][nj] == board[i][j]:
                            while stack:
                                mi, mj = stack.pop()
                                board[mi][mj] = board[i][j]
                            break
                        else:
                            break
        for i in board:
            for j in i:
                print(j, end=' ')
            print()
        print()
    # board 돌면서 1, 2 세기

    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1 += 1
            if board[i][j] == 2:
                cnt2 += 1

    print(f'#{tc} {cnt1} {cnt2}')

