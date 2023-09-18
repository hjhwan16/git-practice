import sys
from collections import deque
sys.stdin = open('input.txt')

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = []
    right = []
    mid = len(arr) // 2
    for i in range(0, mid):
        left.append(arr[i])
    for j in range(mid, len(arr)):
        right.append(arr[j])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):

    result = []
    left_idx = 0
    right_idx = 0
    global ans2
    if left[-1] > right[-1]:
        ans2 += 1
    while len(left) > left_idx or len(right) > right_idx:
        if len(left) > left_idx and len(right) > right_idx:

            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        elif len(left) > left_idx:
            result.append(left[left_idx])
            left_idx += 1
        elif len(right) > right_idx:
            result.append(right[right_idx])
            right_idx += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans2 = 0
    arr = merge_sort(arr)
    # print(arr)
    ans1 = arr[N//2]
    print(f'#{tc} {ans1} {ans2}')