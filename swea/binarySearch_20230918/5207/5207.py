import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    ans = 0
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)
    B = list(map(int, input().split()))

    # B에 있는 숫자를 A행렬 에서 이진탐색
    for i in range(M):
        moving = ''
        flag = [0, 0, 0]
        left = 0
        right = N - 1
        target = B[i]
        flag_in = False
        cnt = 0
        # B[i]를 A 행렬에서 탐색
        while left <= right:
            mid = (left + right) // 2
            # print(A[mid])
            if A[mid] == target:
                ans += 1
                break
            elif A[mid] < target:
                left = mid + 1
                flag[0] = 1
                if moving == 'right':
                    flag_in = False
                    break
                moving = 'right'
            else:
                right = mid - 1
                flag[1] = 1
                if moving == 'left':
                    flag_in = False
                    break
                moving = 'left'

        # print(target, A, flag)
        if flag == [1, 1] and flag_in:
            ans += 1

    print(f'#{tc} {ans}')