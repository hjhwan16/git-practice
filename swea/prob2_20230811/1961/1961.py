import sys
sys.stdin = open('input.txt')

# 숫자배열 회전
# N * N 행렬이 주어 질 때 시계 방향으로 90 / 180 / 270 도 회전한 모양을 출력해라!

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    # 90도 회전
    arr_ninety = []
    for j in range(N):
        temp = []
        for i in range(N-1, -1, -1):
            temp.append(str(arr[i][j]))
        arr_ninety.append(temp)
    # print(arr_ninety)

    # 180도 회전
    arr_half = []
    for i in range(N-1, -1, -1):
        temp = []
        for j in range(N-1, -1, -1):
            temp.append(str(arr[i][j]))
        arr_half.append(temp)
    # print(arr_half)

    #270도 회전
    arr_half_ninety = []
    for j in range(N-1, -1, -1):
        temp = []
        for i in range(N):
            temp.append(str(arr[i][j]))
        arr_half_ninety.append(temp)
    # print(arr_half_ninety)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr_ninety[i]), ''.join(arr_half[i]), ''.join(arr_half_ninety[i]))
    # 그리고 90/180/270 출력
