# 여행 가자 / 20230913
def dfs(arr):
    s = arr[0]-1
    # print(s)
    stack = []
    visited = [0] * (N)
    visited[s] = 1
    while True:
        for v in range(N):
            if adj_m[s][v] == 1 and visited[v] == 0:
                stack.append(s)
                s = v
                # print(s)
                visited[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

    return visited

N = int(input()) # 도시의 수
M = int(input()) # 여행 계획의 수
adj_m = []
for _ in range(N):
    temp = list(map(int, input().split()))
    adj_m.append(temp)
arr = list(map(int, input().split()))



# print(adj_m, arr)
result = dfs(arr)
# print(result)
check = []

for i in range(N):
    if result[i] == 1:
        check.append(i+1)
# print(check)
# print(arr)
if set(arr) & set(check) == set(arr):
    print('YES')
else:
    print('NO')
