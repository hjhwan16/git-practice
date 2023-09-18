# 꽃길 / 20230918
# 모든 경우를 구한 다음 겹치는 경우를 빼고 최소값을 구함.
from itertools import combinations
N = int(input())
arr = []
for _ in range (N):
    temp = list(map(int, input().split()))
    arr.append(temp)
# print(arr)
price = [[-1]*N for _ in range(N)]

test_list = []
for i in range(1, N-1):
    for j in range(1, N-1):
        price[i][j] = arr[i-1][j] + arr[i+1][j] + arr[i][j-1] + arr[i][j+1] + arr[i][j]
        test_list.append([i,j])
# print(price)
# print(test_list)
cnt = 0
combi_list = list(combinations(test_list, 3))
di = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2]
dj = [0, -1, 0, 1, -2, -1, 1, 2, -1, 0, 1, 0]

min_v = 1e9

for i in combi_list:
    temp = 0
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for j in i:
        if visited[j[0]][j[1]] == 0:
            visited[j[0]][j[1]] = 1
            # print(j, end='')
            for k in range(12):
                ni = j[0] + di[k]
                nj = j[1] + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    visited[ni][nj] = 1
            cnt += 1
            temp += price[j[0]][j[1]]
    if cnt == 3:
        # print(temp)
        if min_v > temp:
            min_v = temp
print(min_v)