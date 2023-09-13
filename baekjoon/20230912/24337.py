N, a, b = map(int,input().split())
arr = [1] * N
for i in range(a):
    if arr[i] <= i:
        arr[i] = arr[i-1] + 1

for j in range(b):
    if arr[N-j-1] <= j:
        arr[N-j-1] = arr[N-j] + 1

if (a-1) + (b-1) <= N:
    print(*arr)
else:
    print(-1)
