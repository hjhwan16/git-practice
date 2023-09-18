# 이진 검색 - 반복문

arr = [2, 4, 7, 9, 11, 19, 23]
# 항상 정렬 후 시작
arr.sort()

def binarySearch(low, high, target):
    # 기저 조건 (언제 까지 재귀호출을 반복할 것 인가?)
    if low > high:
        return -1

    mid = (low + high) // 2
    # 1. 가운데 값이 정답인 경우
    if target == arr[mid]:
        return mid
    # 2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        return binarySearch(mid+1, higdh, target)
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch(low, mid-1, target)
