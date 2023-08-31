import sys
sys.stdin = open('input.txt')

def f(board, N):
    global max_v
    if N == 0:
        # print(board)
        s = 0
        for k in range(len(board)):
            s += (board[k]*10**(len(board)-k-1))
        if max_v <= s:
            max_v = s
    else:
        for i in range(len(board)):
            for j in range(i+1, len(board)):
                board[i], board[j] = board[j], board[i]
                f(board, N-1)
                board[i], board[j] = board[j], board[i]


T = int(input())
for tc in range(1, T+1):
    num, M = map(int, input().split())  #숫자판, 교환횟수
    board = list(map(int, str(num)))
    max_v = 0
    idx_arr = [x for x in range(M)]

    if len(board) >= M:
        # print(board, M)
        f(board, M)
        print(f'#{tc} {max_v}')

    else:   # M이 보드의 갯수보다 클 경우 항상 최대를 만들어 줄 수 있음
        board.sort(reverse=True)
        temp = M - (len(board)-1)
        if temp % 2:    # 남은 수가 홀수인 경우 마지막 두개만 바꿔주면 됨.
            board[-1], board[-2] = board[-2], board[-1]
        max_v = 0
        for k in range(len(board)):
            max_v += (board[k]*10**(len(board)-k-1))
        print(f'#{tc} {max_v}')


