# N-queen / 20230919

def backtracking(si, sj, cnt):

    global ans
    # 기저조건
    if len(path) == N:
        ans += 1
        return
    # 반복문과 가지치기
    for k in range(N):
        temp_board = board_list[-1]
        if temp_board[cnt][k] == 1:
            continue

        cnt += 1
        path.append([cnt, k])
        while True:
            i = 0 + cnt
            if i == N:
                break
            temp_board[i][j] = 1
            if i + j < N:
                temp_board[i][j + i] = 1
            if j - i >= 0:
                temp_board[i][j - i] = 1
            i += 1
        board_list.append(temp_board)
        backtracking(cnt, k, cnt)
        path.pop()
        board_list.pop()

N = int(input())
board = [[0] * N for _ in range(N)]
print(board)
board_list= []
ans = 0
for j in range(N):
    board = [[0] * N for _ in range(N)]
    path =[[0, j]]
    i = 1
    while True:
        if i == N:
            break
        board[i][j] = 1
        if i+j < N:
            board[i][j+i] = 1
        if j-i >= 0:
            board[i][j-i] = 1
        i += 1
        board_list.append(board)
    backtracking(0, j, 1)
print(ans)