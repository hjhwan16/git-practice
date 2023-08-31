import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num, M = map(int, input().split())  #숫자판, 교환횟수
    board = list(map(int, str(num)))
    print(board)
    # 제일 최댓값을 제일 왼쪽으로 옮기기
    if len(board) > M:
        # 꼭 바꿀 필요는 없음
        i = 0
        cnt = 0
        while True:
            max_v = board[i]
            max_idx = i
            for j in range(i+1, len(board)):
                if max_v <= board[j]:
                    max_v = board[j]
                    max_idx = j
            if i != max_idx:
                board[i], board[max_idx] = board[max_idx], board[i]
                # print('change', M, cnt, board)
                cnt += 1
            i += 1
            # print(M, cnt, board)
            if cnt == M:
                break
    else:
        for i in range(len(board)):
            max_v = board[i]
            max_idx = i
            for j in range(i+1, len(board)):
                if board[j] > max_v:
                    max_idx = j
            board[i], board[max_idx] = board[max_idx], board[i]
        temp = M - (len(board)-1)
        if temp % 2:
            board[-1], board[-2] = board[-2], board[-1]
    print(f'#{tc}',end = ' ')
    for i in board:
        print(i, end='')
    print()




