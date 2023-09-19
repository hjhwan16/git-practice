import sys
sys.stdin = open('input.txt')

def backtracking(idx, fuel):
    global ans, cnt
    if idx + fuel >= N-1:
        # print(cnt)
        ans = min(cnt, ans)
        return
    for num in range(1, fuel+1):
        if idx + num >= N-1:
            continue
        if cnt > ans: # 가지치기가 중요하다.
            continue
        cnt += 1
        # print('hi')
        backtracking(idx + num, arr[idx + num])
        cnt -= 1



T = int(input())
for tc in range(1, T+1):
    N, *arr = map(int, input().split())
    # print(N, arr)
    ans = 100
    cnt = 0
    nums = [i for i in range(N)]
    # print(nums)
    backtracking(0, arr[0])

    print(f'#{tc} {ans}')

