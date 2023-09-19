import sys
sys.stdin = open('input.txt')

def backtracking(cnt, total):
    global ans
    # 가지치기
    # 기저조건
    if total < ans: # 가지치기는 위쪽에서
        return
    if cnt == N:
        # print(path)
        if ans < total:
            ans = total
        return
    # 반복문 and 가지치기
    for num in range(len(nums)):
        if nums[num] in path:
            continue
        if arr[cnt][nums[num]] == 0:
            continue

        path[cnt] = nums[num]
        total *= arr[cnt][path[cnt]]
        backtracking(cnt+1, total)
        total /= arr[cnt][path[cnt]]
        path[cnt] = -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 직원의 수
    arr = []            # 직원, 일, 성공 확률
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    for i in range(N):
        for j in range(N):
            arr[i][j] *= 0.01
    # print(arr)
    ans = -1
    nums = [i for i in range(N)]
    path = [-1] * N
    backtracking(0, 1)
    print(f'#{tc} {ans*100:.6f}')