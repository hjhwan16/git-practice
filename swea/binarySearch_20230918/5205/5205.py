# 퀵 정렬을 구현해서 N개의 정수를 정렬 해 리스트 A에 넣고 A[N//2]에 저장된 값을 출력

def quicksort(arr, left, right):
    if left < right:
        s = partion(arr, left, right)
        quicksort(arr, left, s-1)
        quicksort(arr, s+1, right)

def partion(arr, left, right):
    p = arr[left]
    i = left
    j = right
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    left = 0
    right = N-1
    quicksort(arr, left, right)
    # arr = sorted(arr)
    print(f'#{tc} {arr[N//2]}')