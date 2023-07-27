# 완전탐색
# 체스판 다시 칠하기
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어진 M * N 크기의 보드를 찾음. 어떤 정사각형은 검은색으로, 나머지는 흰색으로 칠해져 있음
# 이 보드를 잘라서 8 * 8 크기의 체스판으로 만들려고 함.

# 체스판은 검은색과 흰색이 번갈아서 칠해져야 함.
# 두가지 경우가 존재 가능 
# 1. 맨 왼쪽 위칸이 흰색인 경우
# 2. 맨 왼쪽 위칸이 검은색인 경우

# 체스판으로 잘라낸 후에 몇개의 정사각형을 다시 칠함.
# 지민이가 다시 칠해야 하는 정사각형의 최소개수를 구하는 프로그램을 작성.

N, M = map(int, input().split())
chess_list_list = []

# 이중 리스트로 입력 받기
for i in range(N):
    chess_list = list(map(int, input().split()))
    chess_list_list.append(chess_list)

# 경우로 자르기
for j in range(N-7):
    for k in range(i, i+8):
        temp = chess_list_list[k][:M-7]