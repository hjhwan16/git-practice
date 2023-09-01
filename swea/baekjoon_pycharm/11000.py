import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
arr.sort(key=lambda x:(x[0],x[1]))

arr = [[0, 0]] + arr
# print(arr)
ans = 0 # 강의실 갯수
cnt = 0
visited = [0] * (N + 1)
while True:
    S = []
    j = 0
    for i in range(1, N+1):
        if arr[i][0] >= arr[j][1] and visited[i] == 0:
            S.append(arr[i])
            visited[i] = 1
            j = i
            cnt += 1
    ans += 1
    if cnt == N:
        break
print(ans)