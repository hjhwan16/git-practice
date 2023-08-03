import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input()) #덤프 횟수
    arr = list(map(int, input().split()))
    # max_v = arr[0]
    # min_v = arr[0]
    # max_idx = 0
    # min_idx = 0

    # N번동안 max_v와 min_v를 찾아서 max_v-1, min_v+1
    for i in range(N):
        max_v = arr[0]
        min_v = arr[0]
        max_idx = 0
        min_idx = 0
        for j in range(len(arr)):
            if max_v <= arr[j]:
                max_v = arr[j]
                max_idx = j
            if min_v >= arr[j]:
                min_v = arr[j]
                min_idx = j
        # print(max_v-1, min_v+1)
        arr[max_idx] -= 1
        arr[min_idx] += 1
        # print(arr)

    # 다시 최대 최소 찾고 abs 찾기
    max_v = arr[0]
    min_v = arr[0]
    max_idx = 0
    min_idx = 0
    for j in range(len(arr)):
        if max_v <= arr[j]:
            max_v = arr[j]
            max_idx = j
        if min_v >= arr[j]:
            min_v = arr[j]
            min_idx = j
    ans = max_v - min_v
    
    print(f'#{tc} {ans}')