
def dfs(i, j, N, M, d):
    visited = [[0]*M for _ in range(N)]
    print(visited)
    stack = []
    visited[i][j] = 1
    print(i, j)
    tot = arr[i][j]
    while True:
        di = [1, 1, 1]
        dj = [-1, 0, 1]
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and d != k:
                stack.append([i, j, d])
                visited[i][j] = 0
                i, j, d = ni, nj, k
                tot += arr[i][j]
                print(i, j, arr[i][j], tot)
                if ni == N-1:
                    print(f'tot {tot}')
                visited[i][j] = 1
                break
        else:
            tot -= arr[i][j]
            print('pop', i, j, d, arr[i][j], tot)
            if stack:
                temp_lst = stack.pop()
                i = temp_lst[0]
                j = temp_lst[1]
                d = temp_lst[2]
                # tot -= arr[i][j]
                # print('pop', i,j,arr[i][j], tot)

            else:
                break




N, M = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
start_list = []
for i in range(M):
    start_list.append([0, i])
ans = 0

print(start_list)

for start in start_list:
    dfs(start[0], start[1], N, M, -1)

