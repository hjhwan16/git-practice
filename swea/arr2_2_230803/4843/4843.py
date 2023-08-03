# 4843 # 특별한 정렬 # 20230803
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 정수의 갯수
    N = int(input())
    # arr 입력받기
    arr = list(map(int, input().split()))
    for i in range(10):
        max_idx = i
        min_idx = i
        for j in range(i+1, N):
            # i가 짝수인 경우 최댓값
            if i % 2 == 0:
                if arr[max_idx] < arr[j]:
                    max_idx = j
            # i가 홀수인 경우 최솟값
            if i % 2 == 1:
                if arr[min_idx] > arr[j]:
                    min_idx = j
        # 최댓값, 최솟값 변환해주기
        arr[max_idx], arr[i] = arr[i], arr[max_idx]
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    # print(arr)
    ans = ''
    for k in arr[:10]:
        ans += str(k) + ' '

    # print(ans)
    print(f'#{tc} {ans}')