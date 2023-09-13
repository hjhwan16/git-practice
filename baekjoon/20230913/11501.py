# 20230913 / 주식

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = arr[::-1]
    ans = 0
    # print(arr)
    # for i in range(N)
    i = 0
    while True:
        cnt = 1
        for j in range(i+1, N):
            # print(i, arr[i], arr[j])
            if arr[i] > arr[j]:
                cnt += 1
                ans += arr[i] - arr[j]
            else:
                break
        i += cnt

        if i >= N:
            break
    print(ans)

'''
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2

'''
