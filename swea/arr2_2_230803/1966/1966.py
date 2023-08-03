# 1966 / 20230803

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 오름차순 정렬
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    print(f'#{tc}', end=' ')
    for i in arr:
        print(i, end = ' ')
    print()

