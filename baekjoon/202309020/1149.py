# 백트래킹으로 최솟값 뽑기

def backtracking(cnt, s):
    global ans
    if s > ans:
        return
    if len(path) == N:
        ans = min(ans, s)
        return
    for num in range(3):
        if path and path[-1] == num:
            continue
        path.append(num)
        s += arr[cnt][num]
        backtracking(cnt+1, s)
        temp = path.pop()
        s -= arr[cnt][temp]
N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
path = []
ans = 1e9
backtracking(0, 0)
print(ans)