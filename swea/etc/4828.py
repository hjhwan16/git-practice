# min max

T = int(input()) # 테스트케이스 개수
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc}', *arr)
