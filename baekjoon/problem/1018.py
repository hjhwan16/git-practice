import sys
sys.stdin = open('input.txt')
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

# 주어지는 판의 크기
N , M = map(int, input().split())

# 각 경우에서 두가지 경우(왼쪽 위가 흰색 / 왼쪽 위가 검은색)로 칠하는 경우
# 그 경우에서 가장 최소 개수를 print

# 2차원 배열 입력받기
arr = []
for _ in range(N):
    temp = list(input())
    arr.append(temp)


# 모든 경우에서 8 by 8로 자른 다음 리스트에 담기
chess_list = []
for k in range((N-7)*(M-7)):
    for i in range(N-8+1):
        check = []
        for j in range(M-8+1):
            temp = []
            for k in range(8):
                temp.append(arr[i][j+k])
            check.append(temp)
    chess_list.append(check)

print(len(chess_list))