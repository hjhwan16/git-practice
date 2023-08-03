# practice / array2 / 230803목

# 정수 10개를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지 판별하는 하수를 작성.

# 존재하면 1 존재하지 않으면 0

import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트케이스
for tc in range(1, T+1):
    ans = 0
    arr = list(map(int, input().split()))
    # 비트 연산자를 이용한 부분집합구하기
    for i in range(1, 1 << 10): # 공집합은 제외하기 위해 1부터
        tot_temp = 0
        for j in range(10):
            # 부분집합의 합 구하기
            if i & (1 << j):
                tot_temp += arr[j]
                # print(arr[j], end=' ')
        if tot_temp == 0:
            ans = 1
        # print()
    print(f'#{tc} {ans}')