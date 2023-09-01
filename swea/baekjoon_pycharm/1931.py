# 회의실 배정 / 20230901

N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

arr.sort(key=lambda x: (x[1], x[0]))
arr = [[0, 0]] + arr # 초기 상태 만들어 주기

# 초기값
S = []
j = 0
ans = 0
for i in range(1, N+1):

    if arr[i][0] >= arr[j][1]:
        S.append(arr[i])
        j = i   # 마지막 자리 초기화
        ans += 1

print(ans)

