import sys
sys.stdin = open('input.txt')

def backtracking(cnt, total):
    global ans


    if cnt == N:
        # print(path, total)
        if ans > total:
            ans = total
        return

    for i in range(len(nums)):
        if nums[i] in path:
            continue
        if total > ans:
            continue
        path[cnt] = nums[i]
        total += arr[cnt][path[cnt]]
        backtracking(cnt+1, total)
        total -= arr[cnt][path[cnt]]
        path[cnt] = -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # print(arr)
    # 1부터 N까지 순열 구하기
    nums = [i for i in range(0,N)]
    path = [-1]*N
    # print(nums)
    ans = 1e9
    backtracking(0, 0)

    print(f'#{tc} {ans}')