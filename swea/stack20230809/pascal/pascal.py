import sys
sys.stdin = open('input.txt')


# 크기가 N인 파스칼의 삼각형을 출력

T = int(input())

for tc in range(1, T+1):
    # 2차원 배열?
    N = int(input())
    stack = [0] * N
    # 맨 처음은 항상 [1] 로 설정
    stack[0] = [1]

    for i in range(1, N):
        temp = [0] * (i+1)
        # temp 의 처음과 끝은 항상 1로 
        temp[0], temp[i] = 1, 1
        # 1과 i를 제외하고 돌면서 바로위의 두 개의 값을 더한 값을 넣어줌
        for k in range(1, i):
            temp[k] = stack[i-1][k-1] + stack[i-1][k]
        # stack에 추가해줌
        stack[i] = temp

    print(f'#{tc}')
    for i in stack:
        for k in i:
            print(k, end=' ')
        print()

