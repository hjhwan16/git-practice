import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    max_v = arr[0]
    min_v = arr[0]
    for i in range(len(arr)):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
    ans = max_v - min_v
    print(f'#{tc} {ans}')