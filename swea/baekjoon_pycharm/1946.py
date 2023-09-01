# 신입사원 / 20230901
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    arr.sort(key=lambda x: x[0])
    # print(arr)
    ans = 0
    min_v = arr[0][1]
    for i in range(1, N):
        if min_v > arr[i][1]:
            min_v = arr[i][1]
        else:
            ans += 1
    print(N - ans)





'''
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1

'''